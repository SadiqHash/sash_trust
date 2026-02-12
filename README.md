sash_trust

A policy-driven Trust Validation Framework Measuring software trust through enforceable security pillars.

---

What is sash_trust?

Trust is not assumed. Trust is measured.

sash_trust is an open-source trust validation framework designed to evaluate the security posture of software systems using policy-driven security principles.

It analyzes source code and configuration to detect trust-breaking patterns before they reach production.

It does not assume trust.
It verifies it.

---

Why sash_trust Exists

Modern development prioritizes speed.
Security becomes reactive instead of foundational.

Security often becomes:

* “We’ll patch later.”
* “It’s internal.”
* “It’s just a prototype.”

But trust is fragile.
One exposed secret. One insecure configuration. One weak encryption choice.

Common patterns:

* Hardcoded secrets
* Weak encryption
* Debug enabled in production
* Over-permissive access
* Logging sensitive data

These are not theoretical risks.
They destroy trust.

sash_trust exists to make trust measurable, enforceable, and automatable.

---

What sash_trust Solves

Developers want to build secure systems but:

* Don’t always know what to check
* Don’t have time for deep audits
* Rely on assumptions instead of verification

sash_trust provides:

* Policy-driven validation
* Security pillar enforcement
* Structured issue reporting
* Trust score calculation
* CI/CD enforcement capability

---

Security Pillars

sash_trust evaluates software across defined security domains:

* Secure Code Practices
* Encryption Enforcement
* Authentication Integrity
* Secrets Management
* Data Leak Prevention
* Configuration Hygiene

Each detected issue affects the overall Trust Score (0–100).

---

How sash_trust Works

* Loads policy (policies/default.yaml)
* Validates policy schema (sash_trust/policy/schema.py)
* Scans project files (sash_trust/core/scanner.py)
* Applies validators (sash_trust/validators/)
* Aggregates issues (sash_trust/core/result.py)
* Calculates trust score (sash_trust/core/scoring.py)
* Returns structured result

Core engine is interface-agnostic and can be used through:

* Library API
* CLI
* CI adapter

---

Installation

```bash
pip install sash_trust
```
Or via Poetry:

```bash
poetry add sash_trust
```

Usage

CLI

```bash
sash_trust audit ./my_project
```

Example output:

```json
{
  "trust_score": 82,
  "issues": [
    {
      "rule_id": "no-hardcoded-secrets",
      "severity": "high",
      "file": "app.py",
      "line": 14
    }
  ]
}
```

Library

```python
from sash_trust.interfaces.library.api import scan

result = scan("./my_project")
print(result.trust_score)
```

CI Integration (GitHub Actions Example)

```yaml
- name: Run sash_trust
  run: |
    sash_trust audit . --min-score 80
```

Build fails automatically if trust score drops below threshold.


---

What sash_trust Can Solve Today

* Detect hardcoded secrets
* Detect weak hashing algorithms
* Detect insecure debug configurations
* Identify risky logging of sensitive data
* Enforce policy-defined security rules
* More later

---

License

MIT License

---

Contributing

Security tools must be secure themselves.

Before contributing:

* Follow type safety
* Maintain deterministic behavior
* Avoid unsafe defaults
* Write tests