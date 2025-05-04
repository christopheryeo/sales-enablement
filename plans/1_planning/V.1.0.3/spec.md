# Specification: Section Completion Cookies

**Version:** V.1.0.3

## Intended Functionality
- Mark sections as complete when user expands/clicks through them.
- Store an array or object of completed section IDs in a cookie.
- Read cookie on page load to restore progress UI.
- Optionally, allow user to reset progress (clear cookie).

## Technical Scope
- Use `document.cookie` or `localStorage` for persistence (cookie preferred for cross-device).
- Cookie value: JSON array of completed section IDs.
- Update cookie on each section completion event.

## UI Treatments / Layout Options
1. **Checkboxes next to sections:**
   - Checked state persists via cookie.
2. **Progress bar:**
   - Progress bar updates as sections are completed.
3. **Completion badge:**
   - Award a badge when all sections are complete.

## Trade-offs
- **Checkboxes:** Simple and clear, but may clutter UI if many sections.
- **Progress bar:** Clean summary, but less granular.
- **Badge:** Motivational, but adds gamification complexity.
