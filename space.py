#!/usr/bin/python3

import os
import subprocess
import sys

home = os.getenv("HOME")

if len(sys.argv) == 1:
    subprocess.run(["podman", "exec", "-ti", "space", "su", "-Pl"])
else:
    username = sys.argv[1]
    if len(sys.argv) == 2:
        subprocess.run(["podman", "exec", "-ti", "space", "su", "-Pl", username, "-c", "bash"])
    else:
        subprocess.run(["podman", "exec", "-ti", "space", "su", "-Pl", username, "-c"]+sys.argv[2:])
