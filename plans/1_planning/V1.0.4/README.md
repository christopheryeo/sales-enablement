# Quiz Completion Cookies

**Version:** V1.0.4

## Goal
Record quiz completion and scores in cookies to provide feedback, unlock achievements, or recommend further training based on quiz performance.

## Key Requirements
- Track which quizzes a user has completed and their scores.
- Store quiz state and results in cookies for persistence.
- Integrate with feedback and achievement UI.
- Enable future migration to server-side tracking if needed.

## Target Audience
- End users (trainees) taking quizzes.
- Instructors or admins monitoring quiz performance.

## Open Questions
- What data model best captures quiz completion and scores in a cookie?
- How to handle updates if quiz structure changes?
- Should users be able to reset quiz progress?
