# Specification: Quiz Completion Cookies

**Version:** V1.0.4

## Intended Functionality
- Mark quizzes as complete when user submits answers.
- Store quiz IDs and scores in a cookie (JSON object).
- Read cookie on page load to restore quiz completion state.
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
