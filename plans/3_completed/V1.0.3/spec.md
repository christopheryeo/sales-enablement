# Specification: Simplified Progress Tracking

**Version:** V1.0.3 (Revised)

## Intended Functionality
- Reset progress counters each time a user enters the training page
- Increment section count when user expands/clicks through a section
- Update quiz completion count when user correctly answers a quiz question
- Store simple numeric counters in cookies for persistence
- Update both cookies and database with progress information
- Provide visual feedback through checkboxes and progress bars
- Allow users to reset their progress if desired

## Technical Scope
- Use `document.cookie` for persistence (preferred for cross-device compatibility)
- Cookie values: Simple numeric counters for sections viewed and quizzes completed
- Update cookies on each section view and quiz completion event
- Synchronize cookie data with server-side database for admin tracking
- Reset counters on each new training session for consistent experience

## Implementation Details
- On training page load:
  1. Reset the section and quiz counters in the UI
  2. Initialize `sectionsViewed` and `quizzesCompleted` variables to 0
  3. Update the progress meters to show 0 progress

- When a section is viewed:
  1. Increment the `sectionsViewed` counter
  2. Update the cookie with the new count
  3. Send the updated count to the server
  4. Update the progress meter in the UI
  5. Mark the section as viewed with a checkbox (☑)

- When a quiz is completed correctly:
  1. Increment the `quizzesCompleted` counter
  2. Update the cookie with the new count
  3. Send the updated count to the server
  4. Update the quiz score meter in the UI
  5. Provide visual feedback that the answer was correct

- Cookie structure:
  - `smartchat_sections_viewed`: Simple numeric value (e.g., "5")
  - `smartchat_quizzes_completed`: Simple numeric value (e.g., "3")

## UI Elements
1. **Section Progress Meter:**
   - Shows "Progress: X / Y sections viewed"
   - Updates immediately when a section is viewed

2. **Quiz Score Meter:**
   - Shows "Score: X / Y quizzes completed"
   - Updates immediately when a quiz is correctly answered

3. **Section Checkboxes:**
   - Change from ☐ to ☑ when a section is viewed
   - Visual indicator of which sections have been viewed

4. **Reset Button:**
   - Allows users to reset all progress
   - Clears cookies and resets UI elements

## Benefits and Trade-offs
- **Benefits:**
  - Simpler implementation with fewer edge cases
  - More reliable counting mechanism
  - Consistent user experience
  - Clear visual feedback

- **Trade-offs:**
  - Less granular tracking (only counts, not specific sections)
  - Progress resets on each training session (but this is intentional)
  - Requires user to view sections again in each session
