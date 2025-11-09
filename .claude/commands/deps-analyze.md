---
description: Analyze dependencies for security, updates, and optimization opportunities
---

# Dependency Analysis

Comprehensive dependency audit and recommendations.

## Phase 1: Inventory
1. Identify all dependency files:
   - package.json / package-lock.json
   - requirements.txt / Pipfile
   - Gemfile / Gemfile.lock
   - go.mod / go.sum
   - Cargo.toml / Cargo.lock
   - etc.

2. Categorize dependencies:
   - Production dependencies
   - Development dependencies
   - Peer dependencies
   - Optional dependencies

## Phase 2: Security Analysis
1. **Known vulnerabilities**
   - Check for CVEs
   - Severity assessment
   - Available patches

2. **Outdated packages**
   - Current vs latest versions
   - Breaking changes in updates
   - Update priority

3. **Suspicious packages**
   - Unmaintained packages
   - Low download counts
   - Typosquatting risks

## Phase 3: Optimization
1. **Bundle size analysis**
   - Identify large dependencies
   - Find lighter alternatives
   - Tree-shaking opportunities

2. **Redundancy detection**
   - Duplicate functionality
   - Unused dependencies
   - Transitive dependency bloat

3. **Alternative recommendations**
   - More maintained packages
   - Better performance
   - Smaller footprint

## Phase 4: Update Strategy
For each dependency needing updates:
1. **Risk assessment** (breaking changes?)
2. **Update priority** (security > features > optimization)
3. **Testing requirements**
4. **Rollback plan**

## Deliverable
Provide:
- Security vulnerability report
- Prioritized update list
- Optimization opportunities
- Alternative package recommendations
- Update execution plan
