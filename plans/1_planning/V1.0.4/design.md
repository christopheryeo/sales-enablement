# Design Notes: Quiz Completion Cookies

**Version:** V1.0.4

- Use cookies to track exactly which sections a user has read and which quizzes (and answers) they have completed.
- When the user enters the training page, the app will read the cookie and automatically tick checkboxes for all sections they have read and restore answers for all quizzes they have previously attempted.
- Store section and quiz state in cookies for persistence.
- Integrate with feedback and achievement UI.
- Enable future migration to server-side tracking if needed.
- Allow a reset button to clear quiz progress.
- Visual sketch:

```
[User completes quiz] → [Update cookie: add quiz ID + score]
        ↓
[On load: read cookie → update UI]
```

- Component interactions:
  - Frontend updates and reads cookies.
  - Backend may read for analytics if needed in future.
- Consider extensibility for new quizzes or scoring methods.
