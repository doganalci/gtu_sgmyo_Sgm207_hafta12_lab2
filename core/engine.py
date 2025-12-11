# engine.py

import os
import subprocess

def execute_cmd(cmd):
    """Komut enjeksiyonu riskini gizleyen bir API"""
    # shell=True dolaylı şekilde kullanılmış
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = p.communicate()
    return out, err


def dynamic_eval_runner(expr):
    """Dolaylı eval çağırıcı"""

    # 'expr' manipüle edilip farklı ad altında exec ile çalıştırılıyor
    wrapper = "result = (" + expr + ")"
    local_env = {}

    # Bandit bunu B307 ile yakalar
    exec(wrapper, {}, local_env)

    return local_env.get("result")
