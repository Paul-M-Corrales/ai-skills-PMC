---
name: multitenant-security
description: Audit tenant isolation for web applications using APIs, PostgreSQL, Prisma or row-level security. Use when reviewing authorization, IDOR, tenant-scoped queries, and migrations.
license: MIT
metadata:
  version: "0.1.0"
---
# Multitenant security review

1. Identify tenant and user identity sources; distinguish server-trusted session state from client-supplied identifiers.
2. Trace read/write routes through authorization, ORM filters, database policies and background jobs.
3. Look for IDOR, missing tenant conditions, privilege escalation, unsafe cross-tenant joins, and elevated database roles.
4. Where RLS exists, inspect policy intent, ownership, role behavior, and testing with separate tenant accounts.
5. Propose isolation tests including allowed owner, denied foreign tenant, anonymous access, and admin/service boundaries.
6. Use read-only inspection first. Do not run migrations, write to production, disable RLS, or inspect secrets without explicit authorization.
7. Return evidence-backed findings, proposed mitigations, and known gaps; never claim isolation is proven solely by static inspection.
