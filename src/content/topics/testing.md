---
title: Testing in Rails
sample: false
clips:
  - title: Devise testing issue in feature specs
    youtubeId: "fC4QPpgE9BE"
    start: 307
    end: 1697
---

Testing is a recurring thread across the ticketing app streams: RSpec around domain code, ViewComponent specs, custom helpers for Capybara, feature and system tests, FactoryBot with Pundit, and the occasional sharp edge when authentication gems meet the test suite.

Dedicated episodes add **RSpec tests for attendee code**, **refactor and test ViewComponents**, **custom RSpec helpers** for logging users in before feature specs, **feature / system / integration tests** from scratch, and **admin access control with Pundit & FactoryBot**.

The clip above is from a front-end stream that pauses on a **Devise testing issue**—the kind of real-world snag that does not show up in framework docs but blocks your CI until you fix login setup in specs. It sits alongside the longer-running work of building a test suite that matches how the app actually behaves for organisers and ticket buyers.
