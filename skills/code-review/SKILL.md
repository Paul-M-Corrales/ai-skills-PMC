---
name: code-review
description: Review code changes for correctness, regressions, security, performance, and test coverage. Use before merging pull requests or validating a patch.
license: MIT
metadata:
  version: "0.1.0"
---
# Code review

1. Identify the repository, branch, baseline commit, intended scope, and uncommitted changes.
2. Read the relevant diff and nearby code before drawing conclusions.
3. Prioritize provable correctness, security, or data-loss defects over stylistic suggestions.
4. For each finding, provide severity, file and line reference, a reproducible scenario, and the minimal safe fix.
5. Identify missing regression tests; do not assert tests passed unless they were actually executed.
6. Never apply changes, commit, or deploy during a review unless the user authorizes it.
7. If no actionable findings are found, state that and describe remaining uncertainty.
