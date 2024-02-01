#!/usr/bin/python3

import os
import subprocess
import sys

home    = os.getenv("HOME")

container = sys.argv[0]
username = sys.argv[1]

if len(sys.argv) == 2:
    subprocess.run(["podman", "exec", "-ti", "space", "su", "-P", username, "-c", "bash"])
else:
    subprocess.run(["podman", "exec", "-ti", "space", "su", "-P", username, "-c"]+sys.argv[2:])