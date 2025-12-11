# main.py

from core.loader import _dynamic_loader, load_serialized, lazy_operation
from core.crypto_tool import weak_hash, indirect_hash
from core.hidden_ops import suspicious_eval

def main():

    print("=== Advanced Static Analysis Test ===")

    # 1. Dinamik modül & fonksiyon çağırma
    task = _dynamic_loader("plugins.plugin_exec", "run_plugin")
    task("  ls -la ")

    # 2. Zayıf hash
    print("Hash:", weak_hash("admin"))
    print("Hash2:", indirect_hash("password"))

    # 3. Pickle exploit potansiyeli
    data = load_serialized("data/_secrets_internal.dat")
    print("Loaded internal object:", data)

    # 4. Gizli eval çağrısı
    res = suspicious_eval("3 * 7")
    print("Eval result:", res)

    # 5. Dolaylı komut enjeksiyonu
    print(lazy_operation("/etc/passwd"))


if __name__ == "__main__":
    main()
