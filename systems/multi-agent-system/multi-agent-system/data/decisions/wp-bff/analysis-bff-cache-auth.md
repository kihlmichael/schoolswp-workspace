# Analyse Backend : BFF WP REST v2 + Redis + JWT

## Contexte
Endpoint REST WordPress v2 exposé via un BFF (FastAPI).
Décisions passées : pagination cursor-based, TTL différenciés, invalidation webhook HMAC-SHA256.

---

## Architecture globale

```
Client
  │  JWT Bearer token
  ▼
[BFF FastAPI]
  ├── Auth middleware (JWT RS256 / HS256)
  ├── Rate limiter (Redis Sliding Window)
  ├── Cache layer (Redis)
  │     ├── HIT  → retourne payload normalisé
  │     └── MISS → fetch WP REST v2 → normalise → stocke → retourne
  └── WP REST v2 (interne, non exposé)
```

---

## 1. Auth JWT

### Stratégie recommandée : RS256 (asymétrique)
- **Signature** : clé privée côté BFF uniquement
- **Vérification** : clé publique distribuable (JWKS endpoint `/.well-known/jwks.json`)
- **Claims obligatoires** : `sub`, `iat`, `exp`, `jti` (révocation), `scope` (ex: `read:posts`, `write:posts`)
- **Access token TTL** : 15 min — **Refresh token TTL** : 7 jours (stocké Redis avec `jti` pour révocation)

```python
# Middleware FastAPI
from fastapi.security import HTTPBearer
from jose import jwt, JWTError

security = HTTPBearer()

async def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.JWT_PUBLIC_KEY,
            algorithms=["RS256"],
            options={"verify_exp": True}
        )
        # Vérifier révocation via Redis jti
        if await redis.get(f"jwt:revoked:{payload['jti']}"):
            raise HTTPException(403, "Token révoqué")
        return payload
    except JWTError:
        raise HTTPException(401, "Token invalide")
```

### Endpoints publics vs protégés
| Endpoint | Auth | Cache |
|----------|------|-------|
| `GET /posts` | ❌ (public) | ✅ Redis 300s |
| `GET /posts/{slug}` | ❌ (public) | ✅ Redis 600s |
| `POST /posts/invalidate` (webhook) | ✅ HMAC-SHA256 | ❌ |
| `GET /posts/{id}/preview` | ✅ JWT | ❌ (no-cache) |
| `POST /comments` | ✅ JWT | ❌ |

---

## 2. Cache Redis — Stratégie consolidée

### Clés Redis (pattern établi)
```
wp:posts:{page}:{per_page}:{category}:{lang}   TTL 300s   (listing)
wp:post:{slug}                                  TTL 600s   (article)
wp:media:{id}                                  TTL 3600s  (media)
wp:author:{id}                                 TTL 3600s  (auteur)
jwt:revoked:{jti}                              TTL = exp  (révocation JWT)
ratelimit:{ip}:{endpoint}                      TTL 60s    (sliding window)
```

### Cache-aside pattern
```python
async def get_post(slug: str, redis: Redis, wp_client: WPClient):
    cache_key = f"wp:post:{slug}"
    
    # 1. HIT
    if cached := await redis.get(cache_key):
        return PostResponse(**json.loads(cached))
    
    # 2. MISS — fetch parallèle WP
    post = await wp_client.get_post(slug)
    media, author = await asyncio.gather(
        wp_client.get_media(post["featured_media"]),
        wp_client.get_author(post["author"])
    )
    
    # 3. Normalisation + sanitization XSS
    normalized = normalize_post(post, media, author)
    
    # 4. Store avec TTL
    await redis.setex(cache_key, 600, json.dumps(normalized))
    return PostResponse(**normalized)
```

### Invalidation webhook
```python
@router.post("/posts/invalidate")
async def invalidate_cache(request: Request, redis: Redis):
    # Vérification HMAC-SHA256
    signature = request.headers.get("X-WP-Webhook-Signature")
    body = await request.body()
    expected = hmac.new(settings.WP_WEBHOOK_SECRET.encode(), body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(signature, f"sha256={expected}"):
        raise HTTPException(403, "Signature invalide")
    
    payload = await request.json()
    slug = payload.get("post_name")
    
    # Invalidation ciblée + pattern listing
    await asyncio.gather(
        redis.delete(f"wp:post:{slug}"),
        *[redis.delete(k) async for k in redis.scan_iter("wp:posts:*")]
    )
    return {"invalidated": True}
```

---

## 3. Rate Limiting (Redis Sliding Window)

```python
async def rate_limit(ip: str, endpoint: str, redis: Redis, limit=60, window=60):
    key = f"ratelimit:{ip}:{endpoint}"
    now = time.time()
    pipe = redis.pipeline()
    pipe.zremrangebyscore(key, 0, now - window)
    pipe.zadd(key, {str(now): now})
    pipe.zcard(key)
    pipe.expire(key, window)
    _, _, count, _ = await pipe.execute()
    if count > limit:
        raise HTTPException(429, headers={"Retry-After": str(window)})
```

---

## 4. CORS & Sécurité headers

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,  # jamais ["*"] en prod
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
    max_age=3600
)

# Headers sécurité sur chaque réponse
@app.middleware("http")
async def security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Cache-Control"] = "no-store"  # JWT endpoints
    return response
```

---

## Warnings critiques

1. **Preview WP** : les drafts/previews ne doivent JAMAIS être mis en cache Redis — ajouter un flag `no_cache=True` si `status != "publish"`.
2. **Refresh token rotation** : implémenter la rotation (chaque refresh émet un nouveau pair access+refresh, invalide l'ancien `jti`) pour limiter l'exposition en cas de leak.
3. **WP Application Passwords** : si le BFF appelle WP REST v2 en lecture authentifiée (drafts), utiliser WP Application Passwords en Basic Auth sur HTTPS interne — ne jamais exposer ces credentials côté client.
