#!/usr/bin/env python3
import os
import subprocess
import sys

root = "/home/gds/github/gdesmedt1/kamil-hi"
ref = "op://.Gecko's Vault/Cloudflare | Gecko/Gecko Hermes Cloudflare Admin - Account Token/credential"
token = subprocess.check_output(["op", "read", ref], text=True).strip()
env = os.environ.copy()
env["CLOUDFLARE_API_TOKEN"] = token
subprocess.check_call(["npx", "--yes", "wrangler", "deploy"], cwd=root, env=env)