# ✅ FILE: core/secret_loader.py
import json

def load_secrets():
    with open('credentials/credentials.json') as f:
        data = json.load(f)
    return data