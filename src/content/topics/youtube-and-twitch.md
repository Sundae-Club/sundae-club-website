---
title: YouTube and Twitch integration
sample: false
clips:
  - title: Understanding YouTube webhooks and quotas
    youtubeId: "CyTjGWLyUqA"
    start: 243
    end: 1093
  - title: Implementing the PubSubHubbub webhook
    youtubeId: "CyTjGWLyUqA"
    start: 1093
    end: 1546
  - title: Testing the webhook with ngrok
    youtubeId: "CyTjGWLyUqA"
    start: 1546
    end: 2814
  - title: Exploring the Twitch API docs
    youtubeId: "u6cpmIe_uFw"
    start: 186
    end: 625
  - title: Twitch app registration and OAuth
    youtubeId: "u6cpmIe_uFw"
    start: 2321
    end: 3209
  - title: Testing Twitch API requests
    youtubeId: "u6cpmIe_uFw"
    start: 3209
    end: 5341
---

A parallel track in the Sundae Club app connects creators’ **YouTube** and **Twitch** presence to the product: store channel data, import videos, sync metadata, and react to platform events without burning API quota.

Streams start the **YouTube API integration** (with Twitch on the roadmap), **persist channel data** via Active Job, **finish the YouTube importer and Site model**, and **update videos from the app** once per-channel auth works. **YouTube webhooks (PubSubHubbub)** explore push notifications, hub verification, ngrok for local testing, and parsing inbound payloads.

On Twitch, episodes **integrate via the API**, go deeper on **OAuth and EventSub**, and cover **integration testing** once credentials flow. There is even meta fun around **generating YouTube thumbnails in Rails**—on-brand for a channel that livestreams its own development.

Together, these sessions show how to treat external platforms as first-class dependencies in a Rails codebase, not one-off scripts.
