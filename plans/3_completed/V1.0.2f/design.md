# Design Document: V1.0.2f Training Page

## How will we build it?
This document explains the technical approach for building the Training Page, focusing on how the requirements from spec.md will be implemented.

## System Overview
- The Training Page and three additional pages (Homepage, About, Team) will be generated at build-time using content from `content.md`.
- The output will be a static HTML page where cluster headers are always visible (not collapsible), and only the information sections (components) within each cluster are collapsible. Interactive reinforcement questions are included.
- All displayed text on the Training Page will be exactly the same and consistent with the source content in `content.md` (no missing, altered, or inconsistent text), unless minor adjustments are needed for clarity or accessibility.

## Architecture & Components
- The builder script will parse and generate not only the Training Page, but also the Homepage, About, and Team pages/sections from `content.md`, ensuring all content is faithfully rendered in the app.
- **Content Parser**: A custom script or tool will parse `content.md` during the build process, extracting clusters, components, and reinforcement questions. The parser will ensure all text is faithfully transferred to the Training Page, preserving wording, spelling, and formatting.
- **HTML Generator**: The parsed content will be injected into the Training Page template. Cluster headers will always be visible and not collapsible. Only the information sections (components) within each cluster will be collapsible. Question blocks are included as specified. Each section/component will be clearly labeled as in the source.
- **JavaScript Interactivity**: Lightweight JavaScript will handle:
    - Expand/collapse behavior for information sections (components) within each cluster. Cluster headers are always visible and not collapsible.
    - Displaying a 'Questions' button for each section that contains reinforcement questions.
    - By default, reinforcement questions are hidden and only appear when the 'Questions' button is pressed for that section.
    - Show/hide answer functionality for each question.
    - All interactions will be accessible (keyboard, ARIA attributes).
- **Styling/UI**: CSS will ensure the page is visually clear, accessible (keyboard and screen-reader friendly), and responsive for desktop/mobile.

## Data Flow (Build-Time)
1. The build script reads `content.md`, extracting the Training Page and the additional pages (Homepage, About, Team).
2. It parses the markdown into structured data (clusters, components, questions), ensuring all text is transferred without loss or inconsistency.
3. The script generates HTML so that each cluster header is always visible (not collapsible), and each information section (component) within the cluster is collapsible, preserving the structure and labels from `content.md`.
4. For each section with reinforcement questions:
    - The build injects a 'Questions' button into the section.
    - The questions block is hidden by default in the generated HTML.
    - Clicking the button toggles the visibility of the questions block.
    - Each question includes a show/hide answer toggle.
5. The final static HTML, CSS, and JS are bundled for deployment.

## Key Technical Decisions
- **Custom Markdown Parser**: Chosen for reliability and to match the specific structure of `content.md` (generic parsers were not robust for this use-case). The parser will be tested to ensure text consistency and completeness.
- **Build-Time Injection**: Ensures fast page loads and no dependency on runtime markdown parsing. All text is fixed at build-time, guaranteeing consistency.
- **Progressive Enhancement**: All content is visible without JavaScript, but collapsibility and Q&A interactivity require JS.

## Automated Consistency Check
- A dedicated consistency check script (e.g., `content_consistency_check.py`) is included in the workflow.
- This script compares the outline of clusters and components in `content.md` with the detailed training content (between the TRAINING-CONTENT-START and TRAINING-CONTENT-END markers).
- It flags any missing, extra, or mismatched clusters/components, as well as formatting issues (such as missing reinforcement questions or incorrect structure).
- The consistency check is run after content updates and before deployment to ensure the Training Page remains accurate and complete.
- This automated check helps catch structural issues early, supporting robust content management and a reliable user experience.

## Security & Maintainability
- All content is sanitized during the build to prevent XSS and ensure security.
- The design supports easy updates to content by editing `content.md` and rebuilding, with automated checks for text consistency.
- The approach allows for future expansion (e.g., new question types or UI features) with minimal changes.

## Error Handling & Content Structure Enforcement
- The parser and HTML generator must ensure that each component within a cluster is strictly separated and rendered as its own collapsible section, preventing the content from multiple components being lumped together.
- Markdown headings such as reinforcement questions (e.g., `### Reinforcement Question`) must be identified and rendered as interactive question blocks, not as plain text.
- The parser must correctly extract and format reinforcement questions, including their choices and answers, as interactive UI elements.
- Markdown formatting (bold, lists, etc.) within each component and question must be preserved and rendered as HTML for clarity and consistency.
- Automated checks should flag if any component boundaries are missed or if questions are not properly formatted.

## Known Recurring Error: Component Boundary & Question Block Handling
- There is a recurring error where content from multiple components is lumped together under a single cluster, and markdown headings such as '### Reinforcement Question' are rendered as plain text instead of interactive blocks.
- The parser logic must strictly enforce component boundaries: when a new component header is encountered, the previous component must be closed and a new collapsible section started.
- Reinforcement question headings (e.g., '### Reinforcement Question') must be treated as special blocks and never rendered as plain text. They must always trigger the creation of an interactive question UI element.
- Automated tests and content checks must validate that no markdown headings for questions appear as plain text in the final HTML, and that each component's content is isolated and correctly structured.
- Any deviation from this structure should be flagged as a build error and must be fixed before deployment.

## UX & Accessibility Rationale
- Collapsible sections help users focus on one topic at a time, reducing cognitive load.
- Reinforcement questions are hidden by default to keep the interface uncluttered; users can reveal them on demand by pressing the 'Questions' button for a section.
- Interactive questions encourage active learning and self-assessment.
- Keyboard navigation and ARIA attributes will be included for accessibility (including toggling questions and answers).
- All text will be clear, readable, and consistent with the source material, supporting user trust and comprehension.

## Alternatives Considered
- Using a generic markdown parser (rejected: did not handle custom structure well or guarantee text consistency).
- Client-side rendering (rejected: slower and less secure for this use-case).
