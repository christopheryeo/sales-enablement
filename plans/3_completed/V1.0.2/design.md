# Design Notes: User Session Cookies

**Version:** V1.0.2

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

---

## Testing Approach

To ensure the User Session Cookies feature is working as intended:

### Manual Testing
- Open the application in a browser and inspect cookies:
  - On first visit, verify a new session_id cookie is created.
  - Reload the page and confirm the session_id persists.
  - Clear cookies and confirm a new session_id is generated on reload.
- If a session indicator or expiry modal is implemented, verify correct UI behavior (e.g., indicator appears, modal shows on expiry).
- Use browser dev tools to ensure cookies are set with `Secure`, `HttpOnly`, and `SameSite` flags.
- Log out or expire the session (if supported) and verify the session_id is removed or invalidated.

### Automated Testing
- Write backend unit tests (Flask):
  - Test that session_id cookies are set on new sessions and validated on requests.
  - Test that cookies have correct flags and values.
- Write frontend integration tests (e.g., Selenium, Cypress):
  - Simulate user visits, reloads, and session expiries.
  - Check for correct cookie creation and persistence.
- (Optional) Add API endpoint tests to verify backend session validation logic.
