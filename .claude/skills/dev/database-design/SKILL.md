---
name: database-design
description: |
  Aide à concevoir un schéma de base de données : choisir entre PostgreSQL / Neon / Turso / SQLite, sélectionner l'ORM (Drizzle / Prisma / Kysely), poser les index, prévenir le N+1, planifier les migrations safe.
  Utilise ce skill quand l'utilisateur dit : "design de schéma DB", "quel ORM choisir", "PostgreSQL ou SQLite", "index composite", "migration safe", ou avant de poser un nouveau modèle de données.
  NE PAS utiliser pour : du SQL ad-hoc déjà écrit, configurer Supabase Auth (utiliser `nextjs-supabase-auth`), ou pour la couche API au-dessus (utiliser `api-patterns`).
risk: unknown
source: community
date_added: "2026-02-27"
---

# Database Design

> **Learn to THINK, not copy SQL patterns.**

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the request!** Check the content map, find what you need.

| File | Description | When to Read |
|------|-------------|--------------|
| `database-selection.md` | PostgreSQL vs Neon vs Turso vs SQLite | Choosing database |
| `orm-selection.md` | Drizzle vs Prisma vs Kysely | Choosing ORM |
| `schema-design.md` | Normalization, PKs, relationships | Designing schema |
| `indexing.md` | Index types, composite indexes | Performance tuning |
| `optimization.md` | N+1, EXPLAIN ANALYZE | Query optimization |
| `migrations.md` | Safe migrations, serverless DBs | Schema changes |

---

## ⚠️ Core Principle

- ASK user for database preferences when unclear
- Choose database/ORM based on CONTEXT
- Don't default to PostgreSQL for everything

---

## Decision Checklist

Before designing schema:

- [ ] Asked user about database preference?
- [ ] Chosen database for THIS context?
- [ ] Considered deployment environment?
- [ ] Planned index strategy?
- [ ] Defined relationship types?

---

## Anti-Patterns

❌ Default to PostgreSQL for simple apps (SQLite may suffice)
❌ Skip indexing
❌ Use SELECT * in production
❌ Store JSON when structured data is better
❌ Ignore N+1 queries

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.
