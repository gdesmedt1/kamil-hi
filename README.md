# kamil-hi-from-g

Cheeky one-page tribute to **Kamil Rudowski**, built by G.

- Static site in `public/`
- Deployed to Gecko Cloudflare (`geckolabs.workers.dev`)
- Source lives under the `gdesmedt1` GitHub org folder on the VPS

## Deploy

```bash
CLOUDFLARE_API_TOKEN="$(op read 'op://...')" npx --yes wrangler deploy
```

## Live

After deploy: `https://kamil-hi-from-g.geckolabs.workers.dev`