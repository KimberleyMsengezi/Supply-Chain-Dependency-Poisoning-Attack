# Supply-Chain-Dependency-Poisoning-Attack

![Python](https://img.shields.io/badge/Python-3.12-blue) 
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Poisoned-red) 
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-T1195-green) 
![2026](https://img.shields.io/badge/Attack_Chain-2026-orange)

 Offensive security project replicating the exact multi-stage supply-chain attack used in real campaigns (GhostAction, Shai-Hulud, Clinejection). Demonstrates how a single poisoned dependency compromises an entire CI/CD pipeline and exfiltrates secrets in under 60 seconds.

### Executive Summary
Full real-world attack chain targeting modern DevOps environments:
**Dependency Confusion → Malicious Package Installation → Poisoned Pipeline Execution (PPE) → Secret Exfiltration**

Built as a fully reproducible local simulation (no real internet or harmful code).

### Technical Deep Dive ( Techniques)

1. **Dependency Confusion (T1195.002)**  
   Attacker publishes a public package with the same name as an internal one but higher version → `pip install` pulls the malicious version.

2. **Typosquatting + Malicious Wheel**  
   Package `requests-plus` (mimics popular `requests`) uses a malicious `setup.py` + `.pth` hook that executes on import.

3. **GitHub Actions Poisoned Pipeline Execution (PPE)**  
   Hijacked workflow runs arbitrary commands on CI runner, stealing `GITHUB_TOKEN`, secrets, and environment variables.

4. **Cache Poisoning & Secret Exfiltration**  
   Persists across builds and exfiltrates to attacker-controlled endpoint (simulated locally).

### Full Attack Chain Visualization

```mermaid
graph TD
    A[Internal Package Name Collision] --> B[Dependency Confusion on PyPI]
    B --> C[Malicious Package Install via pip]
    C --> D[Post-Install Backdoor Trigger]
    D --> E[Poison GitHub Workflow .yml]
    E --> F[CI Runner Execution PPE]
    F --> G[Steal Secrets + GITHUB_TOKEN]
    G --> H[Exfiltrate to Attacker C2]
