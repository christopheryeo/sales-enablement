# Getting Started with AI Project Management

Welcome! If you’re a programmer new to working with AI or collaborating on large projects, this guide is for you. Here, you’ll learn a simple, organized way to manage your work, keep your team on the same page, and make the most of collaborating with both humans and AI.

---

## Why Use a Structured Approach?

AI projects can move fast and get complicated. Having a clear structure helps everyone:
- Know what’s being worked on
- Find important information quickly
- Track progress and changes
- Collaborate smoothly with teammates and AI tools

---

## How the Project is Organized

The project uses folders and files to keep everything tidy. Here’s what you’ll find:

### 0_backlog/
This is the ideas bin! Drop in any new feature ideas, requests, or cool thoughts. Nothing is too rough—this is where brainstorming happens. Later, the best ideas move forward.

### 1_planning/
This is where the real planning happens for the next release or version. Each version gets its own folder, with three important files:

- **README.md**
  - _What it is:_ A friendly summary of what’s planned for this version.
  - _What to include:_
    - Goals and what you hope to achieve
    - List of main features or changes
    - Why these things matter
    - Key dates or deadlines
    - Links to other docs (like design.md and spec.md)
    - Status (e.g., planning, in progress, done)
  - _Why it matters:_ Anyone (even someone new) can quickly understand what’s going on and where to look for more info.

- **design.md**
  - _What it is:_ The blueprint for how things will work under the hood.
  - _What to include:_
    - Diagrams showing how parts fit together
    - Explanations for big technical decisions
    - How data moves through the system
    - UI sketches or wireframes (if needed)
    - Notes about security, scaling, or connecting to other systems
    - Any trade-offs or alternative ideas you considered
  - _Why it matters:_ Makes sure everyone builds things the same way, and future team members (or AI assistants!) can understand your thinking.

- **spec.md**
  - _What it is:_ The detailed list of what needs to be built and how to know when it’s done.
  - _What to include:_
    - What the system should do (features, user stories)
    - Requirements for speed, security, reliability, etc.
    - Clear criteria for when something is “done”
    - Edge cases or tricky situations to watch for
    - Example test cases
  - _Why it matters:_ Keeps everyone (including AI tools) on the same page about what “finished” looks like.

### 2_inprogress/
(Optional) A place to track things currently being worked on. Helps teams see what’s active and avoid stepping on each other’s toes.

### 3_completed/
When a version is finished, all its files move here. This is your project’s memory—great for audits, onboarding, or learning from the past.

### _reference/
Quick-access docs, like logs of what’s been finished or this very guide!

### _templates/
Handy templates for planning and documenting work. Use these to keep things consistent and easy to read.

---

## What’s the Difference Between spec.md and design.md?

- **spec.md (“Specification”)**
  - _What is it?_ The “what” and “why.” Lists features, requirements, and how you’ll know when you’re done.
  - _What’s inside?_ User stories, requirements, acceptance criteria, test plans, and edge cases.
  - _Who’s it for?_ Anyone who needs to know what is expected: product owners, devs, testers.

- **design.md (“Design”)**
  - _What is it?_ The “how.” Explains how you’ll build what’s in the spec.md.
  - _What’s inside?_ Diagrams, technical decisions, data flows, architecture, and design rationale.
  - _Who’s it for?_ Developers, architects, and future maintainers who need to understand the technical plan.

In short: **spec.md** says what you’re building and what success looks like; **design.md** explains how you’ll build it and why you chose that approach.

---

## Logging Your Prompts

For each version, keep a log of all the prompts (requests, instructions, and decisions) you use while developing. This is done by creating an `ai_prompts_log.md` file in each version’s planning directory (e.g., `plans/1_planning/V1.0.2f/ai_prompts_log.md`).

- **What to log:** Only the prompts you provide (not the AI responses).
- **Why log prompts?**
  - See how many prompts it took to develop each version
  - Create a transparent audit trail of your design and implementation process
  - Help onboard new team members by showing the reasoning and context behind features
  - Enable reproducibility and continuous improvement

This practice is especially useful for AI-assisted development, as it captures the evolution of your thinking and makes your workflow more transparent and measurable.

---

## Tips for Working with AI and Teams

- **Be clear and specific** in your docs—AI tools work best with well-defined requirements.
- **Keep things up to date.** Move ideas and features through the folders as their status changes.
- **Use diagrams and examples**—they help both people and AI understand complex systems.
- **Ask for help!** Don’t hesitate to use AI assistants for brainstorming, documentation, or even code reviews.
- **Review together.** Have regular check-ins to make sure everyone (human and AI) is aligned.

---

## Final Thoughts

A little structure goes a long way, especially in AI projects. By following this system, you’ll:
- Save time searching for info
- Make onboarding new teammates easier
- Avoid misunderstandings
- Build better, faster, and smarter—together with AI

Happy coding and collaborating!

## 3. Workflow

### 3.1. Idea Capture (Backlog)
- All new ideas, feature requests, and enhancements are first documented in `0_backlog/`.
- Ideas are reviewed and prioritized during planning cycles.

### 3.2. Planning
- Selected features are moved to `1_planning/`, organized by target version.
- Each planned version receives detailed documentation:
  - **Design**: System architecture, UX/UI, data flow, and technical decisions
  - **Specification**: Functional and non-functional requirements, test cases, and success criteria

### 3.3. In Progress
- Features under active development may be tracked in `2_inprogress/` (if used).
- This stage supports coordination between team members and helps avoid duplication or conflicts.

### 3.4. Completion & Archiving
- Upon completion, all documentation and artifacts are moved to `3_completed/` under the relevant version.
- A summary and any lessons learned, architecture reviews, or scripts are included for future reference.

### 3.5. Reference & Templates
- The `_reference/` directory provides quick access to logs and methodology.
- The `_templates/` directory ensures all documentation follows a consistent structure, making onboarding and audits easier.

---

## 4. Benefits

- **Clarity & Traceability**: Every idea, design decision, and completed feature is documented and versioned.
- **Iterative Delivery**: Supports agile, incremental releases with clear milestones and documentation.
- **Team Alignment**: Templates and structure ensure all contributors are on the same page.
- **Knowledge Retention**: Completed work and lessons learned are easily accessible for future projects or audits.
- **Adaptability**: The system can be expanded or contracted to fit projects of varying size and complexity.

---

## 5. Best Practices

- Regularly review the backlog and update priorities.
- Keep planning documentation detailed but concise; focus on actionable items.
- Move features promptly between phases to reflect their true status.
- Use the provided templates for all documentation to ensure consistency.
- Archive not just code but also design rationale and lessons learned.

---

## 6. Example: Directory Layout

```
plans/
  0_backlog/
    feature-idea.md
  1_planning/
    V1.0.3/
      README.md
      design.md
      spec.md
    V1.0.4/
      ...
  2_inprogress/
    ...
  3_completed/
    V1.0.2/
      README.md
      design.md
      spec.md
      summary.md
      test_session_cookie.py
  _reference/
    completed_features_log.md
    prodct_management.md
  _templates/
    completed_template.md
    wip_template.md
```

---

## 7. Applicability

This method is suitable for:
- AI/ML projects with evolving requirements
- Software teams needing lightweight but rigorous process
- Startups and research teams balancing speed and documentation

It can be adapted for more formal methodologies (e.g., Scrum, Kanban) or used as a standalone lightweight process.

---

## 8. Conclusion

A structured, versioned, and template-driven approach to project management supports clarity, agility, and long-term knowledge retention, making it ideal for fast-moving AI and software projects.
