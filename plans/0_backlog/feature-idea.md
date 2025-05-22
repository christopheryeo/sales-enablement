# Feature Ideas

Add your raw feature ideas here before they are ready for planning. Use this document to brainstorm and capture new concepts.

---

## Completed Features

These features have been fully implemented and moved to the completed section of the project:

- **Persistent user session cookies** (V1.0.2)
  - Provides secure, persistent session tracking using backend-generated UUID cookies.
- **Interactive training section (collapsible, checklist, progress bar)** (V1.0.2f)
  - Training content is fully interactive, with collapsible sections, visited-section checkboxes, and a progress bar.
- **Reinforcement questions with show/hide answers** (V1.0.2f)
  - Each training section includes reinforcement questions with interactive answer reveal and feedback.
- **Markdown-driven content pipeline**
  - Training and About sections are dynamically populated from markdown (`content.md`) using custom parsing.
- **Admin page for user progress and database management** (V1.0.1)
  - Admin dashboard for tracking user progress, clearing records, and viewing statistics.
- **Vercel deployment configuration and fixes** (V1.0.2h)
  - Ensured Flask app is properly deployed as a Python serverless function on Vercel, resolving 404 errors.
- **Simplified progress tracking with cookies** (V1.0.3)
  - Implemented a counter-based progress tracking system that resets on each training session and increments as users view sections and complete quizzes.
- **Project documentation improvements**
  - README, audit trail, and completed features log are kept up to date with every major release and fix.

---

## Proposed Feature Ideas (2025-05-04)

These features are still in the idea stage and have not yet been planned or implemented:

- **Use cookies to track completion of the first training question** (V1.0.4)
  - As an initial step for V1.0.4, implement cookie-based tracking for whether the user has completed the *first question* of the training page.
  - When the user revisits the training page, the app will read this cookie and visually indicate if the first question was previously completed.
  - This will serve as a pilot for the broader feature of tracking all sections and quizzes.

- **Display app version in menu bar** (V1.0.5)
  - Show the current application version in small font somewhere in the menu bar for quick reference and improved transparency for users and developers.

---

