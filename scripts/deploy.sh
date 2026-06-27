#!/usr/bin/env bash
set -euo pipefail
cd /home/gds/github/gdesmedt1/kamil-hi
export CLOUDFLARE_API_TOKEN="$(op read op://ykhlybw4dkg2nlaac2r2mcmu7e/caslmbddm64e5sdrby7jz335xa/credential)"
exec npx --yes wrangler deploy