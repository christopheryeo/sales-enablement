# Specification: Quiz Completion Cookies

**Version:** V1.0.4

## Intended Functionality
- Use cookies to track exactly which sections a user has read and which quizzes (and answers) they have completed.
- When the user enters the training page, the app will read the cookie and automatically tick checkboxes for all sections they have read and restore answers for all quizzes they have previously attempted.
- Store section and quiz state in cookies for persistence.
- Integrate with the feedback and achievement UI.
- Support future migration to server-side tracking if needed.
- Optionally, allow user to reset quiz progress (clear cookie).

## Technical Scope
- Use `document.cookie` for persistence.
- Cookie value: JSON object mapping quiz IDs to scores/completion state.
- Update cookie on quiz completion event.

## UI Treatments / Layout Options
1. **Quiz completion checklist:**
   - Each completed quiz shows a checkmark.
2. **Score summary modal:**
   - After quiz, show a modal with score and feedback.
3. **Achievement badges:**
   - Award badges for high scores or all quizzes completed.

## Trade-offs
- **Checklist:** Simple and familiar, but may not motivate users.
- **Score modal:** Immediate feedback, but can interrupt flow.
- **Badges:** Motivational, but adds gamification complexity.
