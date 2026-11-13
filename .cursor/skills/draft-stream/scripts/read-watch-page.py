#!/usr/bin/env python3
"""Read a public YouTube watch page. No API key, no local model.

Prints JSON with title, upload date, description, chapter markers, and the
timed caption track. Exits non-zero when the video is not public or the page
does not contain those fields.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request

VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)


def video_id_from(value: str) -> str:
    text = value.strip()
    if VIDEO_ID.fullmatch(text):
        return text
    patterns = [
        r"(?:v=|vi=)([A-Za-z0-9_-]{11})",
        r"youtu\.be/([A-Za-z0-9_-]{11})",
        r"/shorts/([A-Za-z0-9_-]{11})",
        r"/embed/([A-Za-z0-9_-]{11})",
        r"/live/([A-Za-z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    raise SystemExit("Give one public YouTube URL or an 11-character video id.")


def fetch(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-US,en;q=0.9",
            "Cookie": "CONSENT=YES+cb; SOCS=CAISNwgDEgk2NTI3MjYxMzcaAnN2IAEaBgiA_LG4Bg",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read()
    except urllib.error.HTTPError as error:
        raise SystemExit(f"Watch page request failed: HTTP {error.code}") from error


def extract_json_assignment(html: str, name: str) -> dict | None:
    marker = html.find(name)
    if marker < 0:
        return None
    start = html.find("{", marker)
    if start < 0:
        return None
    depth = 0
    in_string = False
    escape = False
    for index in range(start, len(html)):
        char = html[index]
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(html[start : index + 1])
                except json.JSONDecodeError:
                    return None
    return None


def timestamp_to_seconds(value: str) -> int | None:
    parts = value.split(":")
    if not 2 <= len(parts) <= 3:
        return None
    try:
        numbers = [int(part) for part in parts]
    except ValueError:
        return None
    if any(number < 0 for number in numbers):
        return None
    if len(numbers) == 2:
        minutes, seconds = numbers
        if seconds > 59:
            return None
        return minutes * 60 + seconds
    hours, minutes, seconds = numbers
    if minutes > 59 or seconds > 59:
        return None
    return hours * 3600 + minutes * 60 + seconds


def chapters_from_description(description: str) -> list[dict]:
    chapters = []
    for line in description.splitlines():
        match = re.match(
            r"^\s*(?:\d{1,2}:)?\d{1,2}:\d{2}\s+(.+?)\s*$",
            line,
        )
        if not match:
            continue
        stamp = re.match(r"^\s*((?:\d{1,2}:)?\d{1,2}:\d{2})", line)
        if not stamp:
            continue
        start = timestamp_to_seconds(stamp.group(1))
        title = match.group(1).strip(" -")
        if start is None or not title:
            continue
        chapters.append({"title": title, "start": start})
    return chapters


def walk_markers(node, found: list[dict]) -> None:
    if isinstance(node, dict):
        if "chapterRenderer" in node or "macroMarkersListItemRenderer" in node:
            item = node.get("chapterRenderer") or node.get("macroMarkersListItemRenderer")
            title = item.get("title")
            if isinstance(title, dict):
                title = title.get("simpleText") or ""
            time_range = item.get("timeRangeStartMillis")
            if title and isinstance(time_range, int):
                found.append({"title": str(title).strip(), "start": time_range // 1000})
        for value in node.values():
            walk_markers(value, found)
    elif isinstance(node, list):
        for value in node:
            walk_markers(value, found)


def choose_track(tracks: list[dict]) -> dict | None:
    if not tracks:
        return None
    english = [
        track
        for track in tracks
        if str(track.get("languageCode", "")).lower().startswith("en")
    ]
    pool = english or tracks
    asr = [track for track in pool if track.get("kind") == "asr"]
    return (asr or pool)[0]


def transcript_from_track(track: dict) -> list[dict]:
    base = track.get("baseUrl")
    if not isinstance(base, str) or not base.startswith("https://"):
        return []
    url = base + ("&" if "?" in base else "?") + "fmt=json3"
    payload = json.loads(fetch(url).decode("utf-8", "replace"))
    cues = []
    for event in payload.get("events") or []:
        start_ms = event.get("tStartMs")
        segments = event.get("segs") or []
        text = "".join(segment.get("utf8", "") for segment in segments).replace("\n", " ").strip()
        if not text or not isinstance(start_ms, int):
            continue
        cues.append({"start": start_ms // 1000, "text": text})
    return cues


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: read-watch-page.py <youtube-url-or-id>")
    video_id = video_id_from(sys.argv[1])
    html = fetch(f"https://www.youtube.com/watch?v={video_id}&hl=en").decode("utf-8", "replace")
    player = extract_json_assignment(html, "ytInitialPlayerResponse")
    if not player:
        raise SystemExit("The public watch page did not include player data.")
    status = (player.get("playabilityStatus") or {}).get("status")
    reason = (player.get("playabilityStatus") or {}).get("reason") or ""
    if status == "LOGIN_REQUIRED":
        raise SystemExit(
            "YouTube returned a bot check instead of the public watch page. "
            "Do not invent the title, date, or transcript."
        )
    if status not in (None, "OK"):
        raise SystemExit(f"Video {video_id} is not public ({status}: {reason}).")
    details = player.get("videoDetails") or {}
    if details.get("videoId") and details.get("videoId") != video_id:
        raise SystemExit("Watch page video id did not match the requested id.")
    micro = (player.get("microformat") or {}).get("playerMicroformatRenderer") or {}
    if micro.get("isUnlisted") or details.get("isPrivate"):
        raise SystemExit(f"Video {video_id} is not public.")
    title = details.get("title") or micro.get("title") or {}
    if isinstance(title, dict):
        title = title.get("simpleText") or ""
    upload_date = micro.get("uploadDate") or micro.get("publishDate") or ""
    description = details.get("shortDescription") or micro.get("description") or {}
    if isinstance(description, dict):
        description = description.get("simpleText") or ""
    if not title or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(upload_date)):
        raise SystemExit("The public watch page did not include a title and upload date.")
    markers: list[dict] = []
    walk_markers(extract_json_assignment(html, "ytInitialData") or {}, markers)
    chapters = markers or chapters_from_description(str(description))
    deduped = []
    seen = set()
    for chapter in chapters:
        key = (chapter["title"], chapter["start"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(chapter)
    deduped.sort(key=lambda chapter: chapter["start"])
    tracks = (
        ((player.get("captions") or {}).get("playerCaptionsTracklistRenderer") or {}).get(
            "captionTracks"
        )
        or []
    )
    track = choose_track(tracks)
    cues = transcript_from_track(track) if track else []
    if not cues:
        raise SystemExit("The public watch page did not include a timed transcript.")
    json.dump(
        {
            "youtubeId": video_id,
            "title": str(title).strip(),
            "date": upload_date,
            "description": str(description).strip(),
            "chapters": deduped,
            "transcript": cues,
        },
        sys.stdout,
        ensure_ascii=False,
        indent=2,
    )
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
