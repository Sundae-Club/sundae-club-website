---
title: Active Storage in Rails
sample: false
clips:
  - title: Integration strategy for file uploads
    youtubeId: "A9OUSMKyTNY"
    start: 224
    end: 612
  - title: Installing Uppy dependencies
    youtubeId: "A9OUSMKyTNY"
    start: 612
    end: 1726
  - title: Implementing Uppy client code
    youtubeId: "A9OUSMKyTNY"
    start: 1726
    end: 2196
  - title: Form and Active Storage asset configuration
    youtubeId: "A9OUSMKyTNY"
    start: 2196
    end: 2626
  - title: Successful file upload test
    youtubeId: "A9OUSMKyTNY"
    start: 4517
    end: 5300
  - title: Analyzing storage behaviour and UI
    youtubeId: "A9OUSMKyTNY"
    start: 5300
    end: 6412
---

Sundae Club’s event-ticketing Rails app needed drag-and-drop uploads and richer content, so the streams walk through Active Storage from first wiring to a working UI.

Early work adds Active Storage and Action Text for new event fields, then explores Action Text, Active Storage, and Stimulus for richer descriptions. A dedicated session starts from scratch on Active Storage (including making video thumbnails editable), and another stream hooks up dropzone-style avatar uploads.

The deepest dive pairs **Uppy.js** with Rails Active Storage and Stimulus: choosing an integration approach, installing dependencies, building the client-side upload flow, configuring forms and assets, debugging build and versioning issues, and finally confirming a real upload end to end.
