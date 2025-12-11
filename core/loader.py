# loader.py

import importlib
import os
import pickle
import base64


def _dynamic_loader(mod_name, func_name):
    """Dinamik olarak fonksiyon yükleyici (zaafiyet içeriyor)."""

    # Module import injection risk – Bandit B101/B403
    m = importlib.import_module(mod_name)
    f = getattr(m, func_name)

    return f


def load_serialized(path):
    """Pickle dosyasını base64 encode edilmiş gibi gösteriyor."""
    
    with open(path, "rb") as fp:
        raw = fp.read()

    # Zayıf çözme: saldırgan tarafından manipüle edilebilir
    decoded = base64.b64decode(raw)

    # Asıl büyük zafiyet burada: pickle.loads(decoded)
    return pickle.loads(decoded)


def lazy_operation(path):
    """Komut enjeksiyonunu gizleyen bir operasyon."""
    ops = ["ls", "cat " + path, "uname -a"]
    # Çok dolaylı yol ile bir komut seçiliyor
    idx = sum(ord(c) for c in path) % len(ops)

    # Bandit bunu yakalar çünkü os.system içeren fonksiyon engine.py'den geliyor
    from core.engine import execute_cmd
    return execute_cmd(ops[idx])
