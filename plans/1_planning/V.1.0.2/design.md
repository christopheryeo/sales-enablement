# Design Notes: User Session Cookies

**Version:** V.1.0.2

- Use Flask's session or cookie utilities for backend integration.
- Consider a `session_id` UUID stored in a cookie.
- Ensure cookies are set with appropriate flags for security.
- Visual sketch:

```
[User visits site] → [Assign session_id cookie] → [Persist across reloads]
        ↓
[Backend checks session_id on each request]
```

- Component interactions:
  - Frontend sets/reads cookies.
  - Backend validates session and may update session data.
- Consider privacy and compliance (GDPR, etc.).
