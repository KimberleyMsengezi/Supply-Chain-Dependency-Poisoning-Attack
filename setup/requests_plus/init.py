import os
import datetime

def trigger_backdoor():
    print("🔥 ATTACKER CONTROLLED - SUPPLY CHAIN POISONING SUCCESSFUL!")
    print(f"📡 Exfiltrating secrets at {datetime.datetime.now()}")
    
    fake_secrets = {
        "GITHUB_TOKEN": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "AWS_KEY": "AKIAIOSFODNN7EXAMPLE",
        "INTERNAL_API_KEY": "fintech-2026-secret-xyz"
    }
    for k, v in fake_secrets.items():
        print(f"   → {k}: {v} (sent to attacker C2)")
    print("✅ Full pipeline compromise achieved!")
