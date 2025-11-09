---
description: Perform safe refactoring with automated verification and rollback capability
---

# Safe Refactoring Workflow

Execute refactoring with built-in safety checks and verification.

## Pre-Refactoring Checklist
1. ✓ Ensure working directory is clean (or create safety commit)
2. ✓ Run existing tests to establish baseline
3. ✓ Identify all usages of code to be refactored
4. ✓ Document the refactoring plan

## Refactoring Process
1. **Create safety checkpoint**
   - Commit current state or note git hash
   - Document current test results

2. **Execute refactoring**
   - Make changes incrementally
   - Maintain working state at each step

3. **Verification after each step**
   - Run tests
   - Check for type errors
   - Verify build succeeds
   - Search for missed references

4. **Rollback plan**
   - If verification fails, revert to checkpoint
   - Document what went wrong
   - Adjust strategy

## Post-Refactoring Validation
1. ✓ All tests pass
2. ✓ No type errors
3. ✓ Build succeeds
4. ✓ No broken references
5. ✓ Code review checklist:
   - Maintains same behavior
   - Improves code quality
   - No performance regression
   - Documentation updated

## Deliverable
- Clean refactoring with passing tests
- Summary of changes made
- Any issues encountered and resolved
- Recommendations for follow-up refactoring
