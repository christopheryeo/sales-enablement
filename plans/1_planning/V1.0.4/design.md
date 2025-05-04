# Design Notes: Quiz Completion Cookies

**Version:** V1.0.4

- Store quiz completion and scores in a cookie as a JSON object.
- On page load, read cookie and update UI (checklists, badges, etc.).
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
