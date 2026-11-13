---
title: Building a ticketing app
sample: false
clips:
  - title: Welcome and project update
    youtubeId: "Fb6pyRax5CA"
    start: 0
    end: 266
  - title: Modeling ticket requirements
    youtubeId: "Fb6pyRax5CA"
    start: 907
    end: 2147
  - title: Implementing ticket types
    youtubeId: "Fb6pyRax5CA"
    start: 2147
    end: 3399
  - title: Admin controller setup for tickets
    youtubeId: "Fb6pyRax5CA"
    start: 3399
    end: 6112
  - title: Testing and future planning
    youtubeId: "Fb6pyRax5CA"
    start: 6112
    end: 8592
---

Sundae Club’s long-running **event ticketing** arc starts with MVP scoping and modelling decisions, then builds outward: organisations and memberships, the `Event` model, admin UIs to create events, public event pages, editable events, attendees, and the purchase flow.

Streams cover **creating the Event model**, **coding admin create-event UI** (more than once), **making events editable**, **public-facing event pages**, **starting the ticket purchase process**, and **group ticket booking** planning. Prototype work pushes a **ticket buying flow end to end** before the app hardens into something more production-shaped.

The **ticket allocation** session is a concentrated implementation pass: turning requirements into models and ticket types, wiring admin controllers, and leaving room for tests and what comes next. It is representative of how the series balances domain modelling on the whiteboard with incremental Rails code you can ship.
