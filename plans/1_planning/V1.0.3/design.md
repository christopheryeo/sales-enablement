# Design Notes: Section Completion Cookies

**Version:** V1.0.3

- Store completed section IDs in a cookie as a JSON array.
- On page load, read cookie and update UI accordingly.
- Allow a reset button to clear progress.
- Visual sketch:

```
[User completes section] → [Update cookie: add section ID]
        ↓
[On load: read cookie → update checkboxes/progress bar]
```

- Component interactions:
  - Frontend updates and reads cookies.
  - Backend may read for analytics if needed in future.
- Consider scalability if section list changes.
