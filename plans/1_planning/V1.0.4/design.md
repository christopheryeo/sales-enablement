# Design Notes: First Question Completion Cookie

**Version:** V1.0.4

- **Objective**: Track the completion status of only the *first question* in the training page.
- **Mechanism**:
    - A specific cookie, e.g., `training_first_question_done`, will store a boolean value (`true`/`false`).
    - Alternatively, a general progress cookie (e.g., `training_progress`) could store a JSON object, and a key like `first_question_completed: true` would be used. For this initial step, a dedicated cookie is simpler.
- **Behavior**:
    - On completion of the first question (e.g., user clicks "Submit" or "Show Answer" for the first question), the cookie will be set to `true`.
    - When the training page loads, the application will check for this cookie.
    - If the cookie exists and is `true`, a visual indicator (e.g., a checked box, a different styling for the question) will show that the first question has already been addressed.
- **Visual Sketch**:
```
[User interacts with first question (e.g., submits answer)] → [Set cookie 'training_first_question_done' to 'true']
        ↓
[On training page load: read cookie 'training_first_question_done'] → [If 'true', update UI for first question]
```
- **Component Interactions**:
  - Frontend JavaScript will be responsible for setting and reading this specific cookie.
  - No backend interaction is required for this specific feature increment.
- **Extensibility**:
  - While this focuses on the first question, the approach can be extended by using a more complex cookie structure (like the JSON object mentioned above) if the feature expands to track all questions/sections.
- **Reset**:
  - A general "reset training progress" function could clear this cookie along with others. For now, specific reset for just this flag is not a primary concern but can be achieved by clearing the specific cookie.
