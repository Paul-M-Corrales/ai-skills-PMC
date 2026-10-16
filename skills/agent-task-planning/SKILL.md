---
name: agent-task-planning
description: Break down engineering work into bounded agent tickets with acceptance criteria, prerequisites, risk gates, and handoff reports. Use when coordinating parallel coding agents.
license: MIT
metadata:
  version: "0.1.0"
---
# Agent task planning

1. Confirm objective, scope boundaries, current repository and branch, and existing worktree state when available.
2. Produce small tickets with outcomes, touched areas, prerequisites, explicit exclusions, and acceptance criteria.
3. Identify parallelizable work while preventing shared-file and environment conflicts.
4. Mark steps affecting production data, secrets, billing, authorization, or migrations as requiring explicit approval.
5. State validation commands and expected evidence for each ticket.
6. On handoff, report actual work performed, test evidence, open risks, branch/HEAD when verified, and next safe action.
7. Never fabricate execution, tests, commits, approvals, or deployment status.
