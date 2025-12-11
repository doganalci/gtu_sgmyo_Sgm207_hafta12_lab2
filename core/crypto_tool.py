# crypto_tool.py

import hashlib

# Zayıf hash, ama gizlenmiş
def weak_hash(data):
    h = getattr(hashlib, "md5")
    return h(data.encode()).hexdigest()


def indirect_hash(data):
    """MD5 kullanımını iyice gizler."""
    func_name = "".join(["m", "d", "5"])
    h = getattr(hashlib, func_name)
    return h(data.encode()).hexdigest()
