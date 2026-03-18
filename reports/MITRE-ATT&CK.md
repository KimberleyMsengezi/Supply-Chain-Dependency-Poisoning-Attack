# MITRE ATT&CK Mapping - Supply-Chain-Dependency-Poisoning-Attack

| Tactic              | Technique ID | Technique Name                     | Demo in This Project                     |
|---------------------|--------------|------------------------------------|------------------------------------------|
| Initial Access      | T1195.002    | Compromise Software Dependencies   | Dependency confusion + malicious wheel   |
| Execution           | T1059        | Command and Scripting Interpreter  | Post-install .pth hook + workflow run    |
| Credential Access   | T1552        | Unsecured Credentials              | Simulated secret exfiltration in CI      |
| Persistence         | T1546        | Event Triggered Execution          | .pth file persistence                    |
| Exfiltration        | T1041        | Exfiltration Over C2 Channel       | Fake C2 print in payload                 |

**Impact**: Full CI/CD compromise + secret theft in <60 seconds.
