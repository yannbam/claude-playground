---
description: Analyze test coverage and generate comprehensive testing strategy with specific test recommendations
---

# Test Strategy Analysis

Systematically analyze testing approach and identify gaps.

## Phase 1: Current State Assessment
1. Identify testing framework(s) in use
2. Locate all test files and measure coverage
3. Categorize existing tests:
   - Unit tests
   - Integration tests
   - E2E tests
   - Performance tests
4. Calculate coverage metrics (if available)

## Phase 2: Gap Analysis
Identify untested or under-tested areas:
1. **Critical paths** without tests
2. **Edge cases** not covered
3. **Error handling** not validated
4. **Security controls** not verified
5. **Performance characteristics** not measured
6. **Integration points** without tests

## Phase 3: Test Recommendations
For each gap, specify:
1. **What to test** (specific function/flow)
2. **Test type** (unit/integration/e2e)
3. **Test cases** (specific scenarios)
4. **Priority** (critical/high/medium/low)
5. **Complexity** (effort estimate)

## Phase 4: Testing Infrastructure
Review and recommend:
1. Test helpers/utilities needed
2. Mock/stub strategies
3. Test data management
4. CI/CD integration improvements
5. Coverage reporting setup

## Deliverable
Provide:
- Current coverage summary
- Prioritized test backlog with specific test cases
- Testing infrastructure recommendations
- Quick wins (high-value, low-effort tests)
