"""WP REST API security audit helper.

Reads creds from .env. Never echoes secrets back. Writes structured JSON for the
markdown report generator to consume.

Endpoints used (admin-authenticated where available):
- /wp-json/                        : discovery (namespaces + routes count)
- /wp-json/wp/v2/users?context=edit&per_page=100  : users list with roles/capabilities
- /wp-json/wp/v2/plugins           : plugins list (requires install_plugins cap)
- /wp-json/wp/v2/themes            : themes list (active + inactive)
- /wp-json/wp/v2/application-passwords : per-user, requires loop
- /wp-json/wp/v2/types             : post types
- /wp-json/wp/v2/settings          : site options (site_url, admin_email, etc.)

Usage:
    python _wp_audit.py <env_file> <api_url> <output_json>

The env_file is read via python-dotenv. Values are kept in memory only.
"""
import json
import os
import sys
from pathlib import Path

try:
    import requests
    from requests.auth import HTTPBasicAuth
except ImportError:
    print("ERROR: requests not installed. Run: .venv/Scripts/python -m pip install requests python-dotenv")
    sys.exit(2)

try:
    from dotenv import dotenv_values
except ImportError:
    print("ERROR: python-dotenv not installed.")
    sys.exit(2)


def redact(s, keep=4):
    if not s or len(s) < keep + 2:
        return "<short>"
    return f"...{s[-keep:]}"


def fetch(session, url, params=None):
    try:
        r = session.get(url, params=params, timeout=30)
        return {
            "status": r.status_code,
            "ok": r.ok,
            "body": r.json() if r.ok and r.headers.get("content-type", "").startswith("application/json") else None,
            "error": None if r.ok else (r.text[:200] if r.text else "no body"),
        }
    except Exception as e:
        return {"status": None, "ok": False, "body": None, "error": str(e)[:200]}


def main():
    env_file = Path(sys.argv[1]).resolve()
    api_base = sys.argv[2].rstrip("/")
    out_path = Path(sys.argv[3]).resolve()

    if not env_file.exists():
        print(f"ERROR: env file not found: {env_file}")
        sys.exit(3)

    env = dotenv_values(env_file)
    user = env.get("WP_API_USERNAME") or env.get("WP_USER")
    pwd = env.get("WP_API_PASSWORD") or env.get("WP_APP_PASSWORD")

    if not user or not pwd:
        print(f"ERROR: WP_API_USERNAME/PASSWORD not in {env_file}")
        sys.exit(4)

    print(f"audit target: {api_base}")
    print(f"auth user: {user} (password 4-last: {redact(pwd)})")

    session = requests.Session()
    session.auth = HTTPBasicAuth(user, pwd)
    session.headers.update({"User-Agent": "schoolsWP-security-audit/1.0"})

    report = {
        "target": api_base,
        "auth_user": user,
        "auth_pwd_4last": redact(pwd),
        "checks": {},
    }

    print("[1/8] discovery /wp-json/")
    r = fetch(session, f"{api_base}/wp-json/")
    if r["ok"]:
        body = r["body"] or {}
        ns_list = body.get("namespaces", [])
        routes = body.get("routes", {})
        report["checks"]["discovery"] = {
            "status": r["status"],
            "ok": True,
            "name": body.get("name"),
            "description": body.get("description"),
            "url": body.get("url"),
            "home": body.get("home"),
            "namespaces_count": len(ns_list),
            "namespaces": sorted(ns_list),
            "routes_count": len(routes),
            "site_logo": body.get("site_logo"),
            "site_icon": body.get("site_icon"),
            "authentication": body.get("authentication"),
        }
    else:
        report["checks"]["discovery"] = {"status": r["status"], "ok": False, "error": r["error"]}

    print("[2/8] users list (context=edit)")
    r = fetch(session, f"{api_base}/wp-json/wp/v2/users", params={"context": "edit", "per_page": 100, "roles": "administrator,editor,author,shop_manager,fluentcrm_admin,instructor,fluent_boards_admin"})
    if r["ok"]:
        report["checks"]["users_privileged"] = {
            "status": r["status"],
            "ok": True,
            "count": len(r["body"] or []),
            "users": [
                {
                    "id": u.get("id"),
                    "username": u.get("username"),
                    "name": u.get("name"),
                    "email": u.get("email"),
                    "roles": u.get("roles"),
                    "registered_date": u.get("registered_date"),
                    "capabilities_count": len(u.get("capabilities", {})),
                    "extra_capabilities_count": len(u.get("extra_capabilities", {})),
                    "url": u.get("url"),
                }
                for u in (r["body"] or [])
            ],
        }
    else:
        report["checks"]["users_privileged"] = {"status": r["status"], "ok": False, "error": r["error"]}

    print("[2b/8] all users (default context, count only)")
    r = fetch(session, f"{api_base}/wp-json/wp/v2/users", params={"per_page": 1})
    if r["ok"]:
        total = session.head(f"{api_base}/wp-json/wp/v2/users?per_page=1").headers.get("X-WP-Total", "?")
        report["checks"]["users_total"] = {"total_count": total}
    else:
        report["checks"]["users_total"] = {"error": r["error"]}

    print("[3/8] plugins list")
    r = fetch(session, f"{api_base}/wp-json/wp/v2/plugins")
    if r["ok"]:
        plugins = r["body"] or []
        report["checks"]["plugins"] = {
            "status": r["status"],
            "ok": True,
            "count": len(plugins),
            "active": [p for p in plugins if p.get("status") == "active"],
            "inactive": [p for p in plugins if p.get("status") == "inactive"],
        }
    else:
        report["checks"]["plugins"] = {"status": r["status"], "ok": False, "error": r["error"]}

    print("[4/8] themes list")
    r = fetch(session, f"{api_base}/wp-json/wp/v2/themes")
    if r["ok"]:
        themes = r["body"] or []
        report["checks"]["themes"] = {
            "status": r["status"],
            "ok": True,
            "count": len(themes),
            "themes": [
                {
                    "stylesheet": t.get("stylesheet"),
                    "name": (t.get("name") or {}).get("rendered") if isinstance(t.get("name"), dict) else t.get("name"),
                    "version": t.get("version"),
                    "status": t.get("status"),
                    "parent_theme": t.get("template"),
                }
                for t in themes
            ],
        }
    else:
        report["checks"]["themes"] = {"status": r["status"], "ok": False, "error": r["error"]}

    print("[5/8] site settings")
    r = fetch(session, f"{api_base}/wp-json/wp/v2/settings")
    if r["ok"]:
        s = r["body"] or {}
        report["checks"]["settings"] = {
            "status": r["status"],
            "ok": True,
            "url": s.get("url"),
            "title": s.get("title"),
            "description": s.get("description"),
            "language": s.get("language"),
            "timezone": s.get("timezone"),
            "admin_email": s.get("email"),
            "default_role": s.get("default_role"),
            "default_post_format": s.get("default_post_format"),
            "use_smilies": s.get("use_smilies"),
            "show_on_front": s.get("show_on_front"),
            "page_on_front": s.get("page_on_front"),
            "posts_per_page": s.get("posts_per_page"),
            "default_ping_status": s.get("default_ping_status"),
            "default_comment_status": s.get("default_comment_status"),
        }
    else:
        report["checks"]["settings"] = {"status": r["status"], "ok": False, "error": r["error"]}

    print("[6/8] post types")
    r = fetch(session, f"{api_base}/wp-json/wp/v2/types")
    if r["ok"]:
        report["checks"]["post_types"] = {
            "status": r["status"],
            "ok": True,
            "count": len(r["body"] or {}),
            "types": list((r["body"] or {}).keys()),
        }
    else:
        report["checks"]["post_types"] = {"status": r["status"], "ok": False, "error": r["error"]}

    print("[7/8] application passwords (per privileged user)")
    if report["checks"].get("users_privileged", {}).get("ok"):
        app_pwds = []
        for u in report["checks"]["users_privileged"]["users"][:10]:
            ap_r = fetch(session, f"{api_base}/wp-json/wp/v2/users/{u['id']}/application-passwords")
            if ap_r["ok"]:
                pwds = ap_r["body"] or []
                app_pwds.append({
                    "user_id": u["id"],
                    "username": u["username"],
                    "app_passwords_count": len(pwds),
                    "names": [{"name": p.get("name"), "created": p.get("created"), "last_used": p.get("last_used"), "last_ip": p.get("last_ip")} for p in pwds],
                })
            else:
                app_pwds.append({"user_id": u["id"], "username": u["username"], "error": ap_r["error"]})
        report["checks"]["application_passwords"] = {"users": app_pwds}
    else:
        report["checks"]["application_passwords"] = {"skipped": "users_privileged failed"}

    print("[8/8] xmlrpc + login.php exposure check (HEAD only)")
    for path in ["/xmlrpc.php", "/wp-login.php", "/wp-admin/", "/?rest_route=/"]:
        try:
            head = session.head(f"{api_base}{path}", allow_redirects=False, timeout=10)
            r_info = {"status": head.status_code, "location": head.headers.get("Location", ""), "server": head.headers.get("Server", ""), "x_powered_by": head.headers.get("X-Powered-By", ""), "security_headers": {h: head.headers.get(h, "") for h in ["Strict-Transport-Security", "X-Frame-Options", "X-Content-Type-Options", "Content-Security-Policy", "Referrer-Policy", "Permissions-Policy"]}}
            report["checks"].setdefault("exposure", {})[path] = r_info
        except Exception as e:
            report["checks"].setdefault("exposure", {})[path] = {"error": str(e)[:120]}

    print(f"writing report -> {out_path}")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, default=str, ensure_ascii=False)
    print(f"OK: {out_path.stat().st_size} bytes")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    main()
