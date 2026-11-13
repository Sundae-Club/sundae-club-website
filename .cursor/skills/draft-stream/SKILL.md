---
name: draft-stream
description: Draft one new Sundae Club stream page after a livestream is public. Use when given a YouTube URL or video id for a new stream. Reads the public watch page only (no YouTube API key, no local model, no Ollama), writes a single Markdown file under src/content/streams, and leaves it for review.
---

# Draft a stream page

Draft one stream page from one public YouTube video. Stop after that file exists in the working tree.

## Do not

- Call the YouTube Data API, or use a YouTube API key, OAuth token, or `YOUTUBE_API_KEY`.
- Run a local model, Ollama, or any other model server.
- Edit an existing file in `src/content/streams`.
- Create or edit anything in `src/content/topics`.
- Commit a secret, token, `.env` file, or `.wrangler` directory.
- Commit, push, merge, or deploy unless the person explicitly asks in this run. Leave the new file for review.

## Input

Accept one YouTube URL or one 11-character video id. If the person gives more than one video, draft only the first and say the rest were not drafted.

Read the public watch page with the skill script, from the repo root:

```bash
python3 .cursor/skills/draft-stream/scripts/read-watch-page.py 'URL_OR_ID'
```

The script fetches `https://www.youtube.com/watch?v=ID` and that page's public timed-caption URL. It does not use an API key. If it exits non-zero, stop and report the message. Do not invent a title, date, or transcript. A bot-check page is not a transcript. Do not switch to the YouTube Data API, Ollama, or another model to fill the gap.

Use the script's JSON:

- `youtubeId`
- `title`
- `date` (upload date, `YYYY-MM-DD`)
- `description`
- `chapters` when the upload has chapter markers
- `transcript` cues (`start` in seconds, `text`)

## Refuse an existing video

Before writing, search `src/content/streams` for `youtubeId: "<id>"`. If any file already has that id, stop and report the path. Do not change that file.

Also refuse when the destination path already exists, even if the id differs.

## File

Write one file only:

`src/content/streams/YYYY-MM-DD-slug.md`

`YYYY-MM-DD` is the upload date from the watch page. The slug is the title in lowercase. Replace each apostrophe with a hyphen (`we're` becomes `we-re`, `let's` becomes `let-s`). Replace every other character that is not `a-z` or `0-9` with a hyphen. Collapse repeated hyphens, then trim hyphens from the ends. The page URL is `/streams/YYYY-MM-DD-slug`.

Match the stream schema in `src/content.config.ts`. Frontmatter only, no Markdown body. Quote titles and the summary. `start` is an integer number of seconds. `sample` stays unset.

```yaml
---
title: "Stream title"
date: 2024-10-11
youtubeId: "xxxxxxxxxxx"
summary: "One to three sentences."
topics:
  - hotwire
chapters:
  - title: "Opening"
    start: 0
---
```

When no existing topic fits, use `topics: []`.

## Summary, topics, and chapters

Write the summary from the title and the timed transcript. One to three sentences. Do not paste the transcript into the file, and do not state a fact that is not in the title, description, or transcript.

Topic labels are slugs of files that already exist in `src/content/topics` (`active-storage`, `email`, `hotwire`, `onboarding`, `sketch-ui`, `stimulus`, `tailwind`, `testing`, `ticketing`, `view-components`, `youtube-and-twitch`, or a later file in that directory). Read the directory. Add a slug only when the transcript is about that topic. Do not create a topic page to make a label fit.

When `chapters` from the script is non-empty, use those markers and no others. When it is empty, write one chapter whose title is the stream title and whose `start` is `0`.

## After writing

Show the path and the frontmatter. Say that the file is uncommitted and was not deployed. Stop.
