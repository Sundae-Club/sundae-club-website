# sundae-club-website

Static site for [sundaeclub.co](https://sundaeclub.co), built with [Astro](https://astro.build). `npm run build` writes the site to `dist/`. `npm run pages:deploy` builds that static output and uploads it to the Cloudflare Pages project `sundae-club` (production branch `main`). The public hostname is the apex `https://sundaeclub.co`, not `pages.dev`.

## Run locally

```bash
npm install
npm run dev
```

The dev server prints a local URL, usually http://localhost:4321.

Use Node 22.23.5. Astro 7 does not run on Node 20.

To preview the production build:

```bash
npm run build
npm run preview
```

## Deploy to Cloudflare Pages

Use Node 22.23.5. From this repo, authenticate once in a terminal (this opens Cloudflare's login in the browser; do not paste a token into chat):

```bash
npx wrangler login
```

Then build and upload `dist/`:

```bash
npm run pages:deploy
```

The script creates the Pages project `sundae-club` if it is missing, then deploys the static `dist/` directory as the `main` production branch. It passes Wrangler's `--force` so this site stays on Cloudflare Pages. That upload is served at `https://sundae-club.pages.dev` until the apex domain is attached. The site to use is `https://sundaeclub.co`. `www` is not added.

Wrangler 4.161 has no `pages domain` command. Attach the apex in the dashboard after deploy:

1. Workers & Pages → `sundae-club` → Custom domains → Set up a domain → `sundaeclub.co`.
2. An apex domain has to be a zone on the same Cloudflare account as the Pages project. Confirm `sundaeclub.co` is on that account before continuing.
3. If the zone is already on the account, continue. Cloudflare creates a proxied CNAME at the apex (`sundaeclub.co`, name `@`) pointing at `sundae-club.pages.dev`.
4. If the zone is not on the account, add the site in the Cloudflare dashboard (Websites → Add a domain → `sundaeclub.co`). Cloudflare shows two assigned nameservers. At the registrar, replace the domain's nameservers with that pair. Do not guess the nameserver hostnames, and do not change them from this repo. When the zone is active, repeat step 1. Cloudflare then creates the same proxied apex CNAME to `sundae-club.pages.dev`.
5. The certificate can stay pending after the domain is attached. That is SSL issuance, not a failed deploy. `https://sundaeclub.co` is ready once the custom domain status is active.

## Content

Streams are Markdown files in `src/content/streams`, named `YYYY-MM-DD-slug.md`, and are served at `/streams/YYYY-MM-DD-slug`. Topics are hand-written Markdown files in `src/content/topics`, named `slug.md`, and are served at `/topics/slug`.

The files there now are samples. Replace them. Chapter and clip times are in seconds. Video fields are YouTube ids only — the site embeds the player and does not call the YouTube API.
