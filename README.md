# sundae-club-website

Static site for [www.sundaeclub.co](https://www.sundaeclub.co), built with [Astro](https://astro.build). `npm run build` writes the site to `dist/` for a later static publish. This repo does not deploy it.

## Run locally

```bash
npm install
npm run dev
```

The dev server prints a local URL, usually http://localhost:4321.

To preview the production build:

```bash
npm run build
npm run preview
```

## Content

Streams are Markdown files in `src/content/streams`, named `YYYY-MM-DD-slug.md`, and are served at `/streams/YYYY-MM-DD-slug`. Topics are hand-written Markdown files in `src/content/topics`, named `slug.md`, and are served at `/topics/slug`.

The files there now are samples. Replace them. Chapter and clip times are in seconds. Video fields are YouTube ids only — the site embeds the player and does not call the YouTube API.
