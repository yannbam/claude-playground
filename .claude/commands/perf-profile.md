---
description: Performance analysis and optimization recommendations
---

# Performance Profiling & Optimization

Systematic performance analysis and optimization workflow.

## Phase 1: Baseline Measurement
1. **Identify performance metrics**
   - Response times
   - Throughput
   - Memory usage
   - CPU usage
   - Bundle size (for web apps)
   - Load times

2. **Establish current baseline**
   - Run performance tests
   - Document current metrics
   - Identify performance goals/SLAs

## Phase 2: Bottleneck Identification
1. **Analyze critical paths**
   - Hot code paths
   - Frequently called functions
   - Large data processing loops

2. **Common performance issues**
   - N+1 queries
   - Missing indices
   - Inefficient algorithms (O(n²) → O(n log n))
   - Memory leaks
   - Unnecessary re-renders
   - Blocking operations
   - Large bundle sizes
   - Unoptimized images/assets

3. **Profiling analysis**
   - CPU profiling points
   - Memory allocation patterns
   - I/O wait times
   - Database query performance

## Phase 3: Optimization Opportunities
Categorize by impact and effort:

**Quick Wins** (high impact, low effort):
- Caching opportunities
- Index missing columns
- Lazy loading
- Code splitting

**Strategic** (high impact, high effort):
- Algorithm improvements
- Architecture changes
- Database restructuring

**Nice-to-have** (low impact, low effort):
- Micro-optimizations
- Code cleanup

## Phase 4: Optimization Plan
For each optimization:
1. **Expected improvement**
2. **Implementation complexity**
3. **Risk assessment**
4. **Measurement strategy**

## Deliverable
- Current performance baseline
- Prioritized optimization backlog
- Expected improvements
- Implementation recommendations
- Performance testing strategy
