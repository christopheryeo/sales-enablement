# Design Notes: Simplified Progress Tracking

**Version:** V1.0.3 (Revised)

## Core Design
- Use simple numeric counters for tracking progress
- Reset counters on each training page load
- Increment counters when sections are viewed or quizzes completed
- Store counters in cookies for persistence
- Synchronize with server for admin tracking
- Visual sketch:

```
[User enters training page] → [Reset counters in UI]
                ↓
[User views section] → [Increment section counter → Update cookie and UI]
                ↓
[User completes quiz] → [Increment quiz counter → Update cookie and UI]
```

## Implementation Details
- Cookie names:
  - `smartchat_sections_viewed`: Simple numeric value
  - `smartchat_quizzes_completed`: Simple numeric value
- Cookie expiration: 365 days
- JavaScript functions:
  - `setCookie(name, value, days)`: Sets a cookie with expiration
  - `getCookie(name)`: Gets a cookie by name
  - `deleteCookie(name)`: Deletes a cookie
  - `incrementSectionCount()`: Increments section count and updates cookie
  - `incrementQuizCount()`: Increments quiz count and updates cookie
  - `resetProgress()`: Resets all progress counters and cookies
  - `updateProgressUI()`: Updates UI based on current counter values

## Data Flow
1. On training page load:
   - Reset `sectionsViewed` and `quizzesCompleted` counters to 0
   - Update UI to show 0 progress
   - Initialize event listeners for sections and quizzes

2. When user views a section:
   - Increment `sectionsViewed` counter
   - Update cookie with new count
   - Send count to server via AJAX
   - Update progress meter in UI
   - Mark section as viewed (checkbox ☑)

3. When user correctly answers a quiz:
   - Increment `quizzesCompleted` counter
   - Update cookie with new count
   - Send count to server via AJAX
   - Update quiz score meter in UI
   - Show correct answer feedback

4. When user clicks reset button:
   - Reset both counters to 0
   - Delete cookies
   - Reset UI elements (uncheck all checkboxes, reset progress meters)
   - Notify server of reset

## Component Interactions
- Frontend manages counters and updates cookies
- Frontend sends progress updates to backend via AJAX
- Backend stores progress for analytics and admin reporting
- UI provides immediate visual feedback for user actions
- Simple numeric values avoid complex data structures and parsing issues
