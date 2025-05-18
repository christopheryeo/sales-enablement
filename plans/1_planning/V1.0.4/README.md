# Quiz Completion Cookies

**Version:** V1.0.4

## Goal
Use cookies to track the exact sections that have been read and quizzes that have been completed by the user. When the user enters the training page, the app will read the cookie and automatically tick checkboxes for all sections they have read and restore answers for all quizzes they have previously attempted.

## Key Requirements
- Track exactly which sections a user has read and which quizzes (and answers) they have completed.
- Store section and quiz state in cookies for persistence.
- When entering the training page, restore all previously read sections as checked and restore quiz answers.
- Integrate with feedback and achievement UI.
- Enable future migration to server-side tracking if needed.

## Target Audience
- End users (trainees) taking quizzes.
- Instructors or admins monitoring quiz performance.

## Open Questions
- What data model best captures quiz completion and scores in a cookie?
- How to handle updates if quiz structure changes?
- Should users be able to reset quiz progress?
