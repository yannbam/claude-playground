---
description: Comprehensive security vulnerability scan and security best practices audit
---

# Security Audit

Perform a systematic security review covering OWASP Top 10 and common vulnerabilities.

## Scan Categories

### 1. Injection Vulnerabilities
- SQL injection points
- Command injection risks
- Code injection vectors
- XSS vulnerabilities (reflected, stored, DOM-based)
- Template injection

### 2. Authentication & Authorization
- Weak password policies
- Insecure session management
- Missing authentication checks
- Broken access controls
- JWT/token vulnerabilities

### 3. Sensitive Data Exposure
- Hardcoded secrets/credentials
- Unencrypted sensitive data
- Insecure data transmission
- Exposed API keys
- Debug information leakage

### 4. Dependencies & Configuration
- Known vulnerable dependencies (check package.json, requirements.txt, etc.)
- Security misconfigurations
- Unnecessary services/features enabled
- CORS misconfiguration

### 5. Business Logic
- Race conditions
- Insecure direct object references
- Mass assignment vulnerabilities
- Insufficient rate limiting

### 6. File Operations
- Path traversal vulnerabilities
- Unsafe file uploads
- Insecure deserialization

## Process
1. Search for common vulnerability patterns
2. Review authentication/authorization code
3. Check for hardcoded secrets
4. Analyze dependency security
5. Review API endpoints for access controls

## Deliverable
Provide prioritized findings with:
- Severity (Critical/High/Medium/Low)
- Location (file:line)
- Vulnerability description
- Exploitation scenario
- Remediation steps
