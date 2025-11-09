---
description: Systematic debugging workflow for investigating and resolving complex issues
---

# Debug Trace Workflow

Systematic approach to debugging complex issues.

## Phase 1: Issue Definition
1. **Reproduce the issue**
   - Document exact steps to reproduce
   - Note expected vs actual behavior
   - Identify error messages/symptoms

2. **Gather context**
   - When did this start?
   - What changed recently?
   - Does it happen consistently?
   - Any related logs or error traces?

## Phase 2: Hypothesis Formation
1. **Analyze error messages**
   - Stack traces
   - Error codes
   - Log patterns

2. **Code flow analysis**
   - Trace execution path
   - Identify decision points
   - Map data transformations

3. **Generate hypotheses**
   - List possible root causes
   - Rank by likelihood
   - Identify tests for each hypothesis

## Phase 3: Systematic Investigation
For each hypothesis (highest likelihood first):
1. **Locate relevant code**
2. **Analyze logic**
3. **Test hypothesis**
   - Add logging/debugging
   - Create minimal reproduction
   - Test edge cases

4. **Confirm or reject**
   - Document findings
   - Move to next hypothesis if rejected

## Phase 4: Resolution
1. **Implement fix**
2. **Verify fix resolves issue**
3. **Check for regressions**
4. **Add test to prevent recurrence**

## Phase 5: Root Cause Analysis
Document:
- What was the bug?
- Why did it occur?
- How was it missed?
- How can similar bugs be prevented?

## Deliverable
- Root cause identified
- Fix implemented and tested
- Prevention measures added
- Documentation updated
