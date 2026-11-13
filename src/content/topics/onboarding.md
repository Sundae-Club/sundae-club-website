---
title: User onboarding
sample: false
clips:
  - title: Planning the wizard sign-up flow
    youtubeId: "3FwW0NY2pdE"
    start: 168
    end: 492
  - title: Designing the onboarding steps
    youtubeId: "3FwW0NY2pdE"
    start: 492
    end: 1137
  - title: Building the skeleton setup
    youtubeId: "3FwW0NY2pdE"
    start: 1137
    end: 1946
  - title: Handling multi-step state in controllers
    youtubeId: "3FwW0NY2pdE"
    start: 4065
    end: 5080
  - title: Discussing multi-step wizard patterns
    youtubeId: "d-4DkTq3e2s"
    start: 717
    end: 1205
  - title: Implementing user onboarding end to end
    youtubeId: "d-4DkTq3e2s"
    start: 2816
    end: 4840
---

The Sundae Club app treats onboarding as a **multi-step wizard**, not a single Devise form. Streams sketch the flow (often on a jam board), add step-by-step sign-up in Rails, then layer on organisation details, UI polish, and controller logic that keeps state across steps.

**Adding step-by-step (wizard) sign up** covers planning the flow, designing each step, scaffolding routes and views, implementing the organisation form, and wiring controllers so users can move forward (and backward) without losing context.

Follow-on episodes **finish** and **tidy up** onboarding: reviewing existing code, debating how wizards should behave, building the details controller, and creating the user only after related records (like a site) exist. Later work adds more UI and business rules inside the same wizard pattern.

If you are designing sign-up for a real product—not just `User.create!` in one request—these sessions are a practical playbook for Rails.
