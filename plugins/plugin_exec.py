# plugin_exec.py

import subprocess

def run_plugin(arg):
    """Argümana göre zararsız gibi görünen ama komut enjekte eden plugin"""
    transform = lambda s: s.replace("safe", "").strip()

    final_cmd = "echo safe | " + transform(arg)

    # shell=True dolaylı olarak riskli
    subprocess.call(final_cmd, shell=True)
