#!/usr/bin/env python3
"""Run Claude's validator on the plugin and the marketplace, and optionally build dist/personal-trainer.plugin.
python3 check.py [--build]"""
import subprocess, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGIN = ROOT / "personal-trainer"
subprocess.run(["claude", "plugin", "validate", str(PLUGIN)], check=True)
subprocess.run(["claude", "plugin", "validate", str(ROOT)], check=True)
if "--build" in sys.argv:
    out = ROOT / "dist/personal-trainer.plugin"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(PLUGIN.rglob("*")):
            if f.is_file() and f.name != ".DS_Store" and "__pycache__" not in f.parts:
                z.write(f, f.relative_to(PLUGIN))
    print("built", out)
