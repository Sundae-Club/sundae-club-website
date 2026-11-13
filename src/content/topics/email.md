---
title: Email in Rails
sample: false
clips:
  - title: Factors to consider when picking an ESP
    youtubeId: "Zz5fxj-756k"
    start: 440
    end: 525
  - title: Choosing an email provider
    youtubeId: "Zz5fxj-756k"
    start: 1105
    end: 1280
  - title: Setting up SparkPost
    youtubeId: "Zz5fxj-756k"
    start: 1280
    end: 1700
  - title: Adding and verifying a sending domain
    youtubeId: "Zz5fxj-756k"
    start: 1725
    end: 2050
  - title: Configuration sets and bounce handling
    youtubeId: "Zz5fxj-756k"
    start: 2805
    end: 3160
  - title: Requesting production access
    youtubeId: "Zz5fxj-756k"
    start: 3160
    end: 5168
---

Email shows up throughout the ticketing app build: account flows that touch the user’s address, local development tooling, actually sending mail from the app, and eventually wiring a real email service provider.

One stream explores **email gems for local development** alongside pub/sub patterns in Rails—useful when you want to develop and test mail without blasting real inboxes. Another session focuses on **sending emails from the Rails app** once the basics are in place.

The most structured walkthrough is **adding an ESP**: comparing providers on price, support, and link tracking, choosing SparkPost, walking through DNS (TXT records), AWS configuration sets, and feedback for bounces and complaints before requesting production access. Together, those streams trace a path from “emails work on my machine” to something you could run in production.
