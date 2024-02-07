#!/usr/bin/python3

import os
import subprocess
import sys

home = os.getenv("HOME")

if len(sys.argv) == 1:
    subprocess.run(["podman", "exec", "-ti", "space", "sudo", "-i"])
else:
    username = sys.argv[1]
    subprocess.run(["podman", "exec", "-ti", "space", "sudo", "-iu", username]+sys.argv[2:])
