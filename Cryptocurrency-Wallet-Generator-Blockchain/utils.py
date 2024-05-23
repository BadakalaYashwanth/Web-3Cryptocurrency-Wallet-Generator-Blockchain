# utils.py

import hashlib
import json

def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()

def json_dumps(obj):
    return json.dumps(obj, sort_keys=True, indent=4)
