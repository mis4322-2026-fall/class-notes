# Grading and Assessment Strategy (Draft v0.1)

This policy is designed to be easy for students to understand and easy for the instructor to run consistently.

## 1) Attendance Requirement (Pass/Fail Gate)

- Students must attend at least 75% of class sessions.
- If attendance is below 75%, the student fails the course regardless of points earned in other categories.
- Attendance is tracked per class session (present/absent).

This is a course-completion requirement, not a points category.

## 2) Grade Components (100 Points Total)

| Component | Weight | Why It Exists |
| --- | ---: | --- |
| Exams (3 paper exams) | 55% | Primary measure of individual conceptual and technical understanding under controlled conditions. |
| Homework (exercise-based) | 10% | Low-stakes practice and completion accountability; students can use AI while preparing for exam understanding. |
| Course Project | 25% | Demonstrates independent mastery through applied work. |
| Participation (commit activity) | 10% | Rewards consistent engagement and active course workflow. |

## 3) Exams (55%)

- There are 3 exams, weighted equally within the exam category (55% total).
- Exams are paper-based and drawn from the chapter assessment question bank.
- Suggested chapter grouping:
  - Exam 1: Chapters 1-4
  - Exam 2: Chapters 5-9
  - Exam 3: Chapters 10-13
- Exam questions should include:
  - conceptual understanding
  - code-reading interpretation
  - short applied reasoning based on class topics

## 4) Homework (10%)

- Homework is based on selected section exercises.
- Students may use AI tools for homework.
- Homework is graded for correctness/completion only.
- Homework is intentionally low weight so students are motivated to build true understanding for exams.
- Simple homework rubric (per assignment):
  - 100% correctness/completion

### Recommended Homework Schedule (Selective)

Not every chapter needs homework. Use homework where practice volume has the biggest learning payoff.

| Chapter | Homework Recommendation | Rationale |
| --- | --- | --- |
| 1 | Optional / in-class only | Setup and onboarding are better handled live. |
| 2 | Optional / in-class only | Git workflow can be reinforced through participation commits. |
| 3 | Homework required | Core data-structure fluency needs repetition. |
| 4 | Homework required | Function design and lambdas improve with repeated practice. |
| 5 | Optional | Can be assessed through exams and selected class activities. |
| 6 | Optional | Lightweight reinforcement if API/JSON skills need support. |
| 7 | Homework required | NumPy/Pandas skills benefit from hands-on work outside class. |
| 8 | Optional | Keep focus on interpretation; not heavy coding practice. |
| 9 | Optional | SQL bridge can be measured well in exams. |
| 10 | Optional | Flask concepts can be kept low-stakes before OOP deep dive. |
| 11 | Homework required | OOP modeling needs individual practice before project work. |
| 12-13 | No standalone homework | Learning evidence is captured through the course project. |

Practical cadence:

- Plan 4 required homework checkpoints tied to Chapters 3, 4, 7, and 11.
- Optionally add 1 bonus or recovery homework from Chapters 5, 6, or 9.
- Keep Chapters 12-13 focused on project milestones rather than separate homework submissions.

## 5) Participation via Commits (10%)

Participation is tracked from Git commit history (timestamped commits).

To keep this fair and low-maintenance, score participation by active weeks instead of raw commit count.

- Define an "active week" as a week with at least 2 meaningful commits on coursework.
- Participation score = (active weeks / total course weeks) * 10 points, capped at 10.
- The instructor can use a script to pull commit timestamps and summarize weekly activity.

Recommended guardrails:

- Multiple tiny commits in one minute should not automatically count as higher participation.
- Commits should represent real progress (exercise work, notes updates, refactors, project steps).

## 6) Course Project (25%)

The project follows a lightweight SDLC deliverable model that is AI-assisted and artifact-driven.

Required parts:

- Acceptance Criteria (`ACCEPTANCE_CRITERIA.md`)
- AI Spec Prompt (`AI_SPEC_PROMPT.md`)
- Working web artifact (Django app)
- Reproducible run instructions (`RUN.md`)
- Implementation checklist (`FEATURE_CHECKLIST.md`)
- AI change log (`AI_USAGE.md`)
- Screenshots for key flows

Optional bonus part:

- Hosting deployment URL + deployment notes

Project grading should use the project rubric in `site/project-sports-analytics-django/PROJECT_GRADING_RUBRIC.md`.

Local-run gate expectation:

- App runs locally from `RUN.md`
- Login works
- At least one protected report page works

If local-run gate is not met, apply the rubric cap policy.

## 7) Final Grade Calculation

1. Verify attendance gate first (must be >= 75%).
2. Compute weighted score out of 100 from Exams + Homework + Project + Participation.
3. Convert to letter grade (suggested scale):

| Numeric | Letter |
| ---: | --- |
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| <60 | F |

## 8) Instructor Workflow (Keep It Sustainable)

- Weekly:
  - Mark attendance.
  - Run commit-summary script and update participation tracker.
- Per module/chapter block:
  - Grade selected homework batch.
- At 3 checkpoints:
  - Administer and grade exams from existing assessment bank.
- End of term:
  - Evaluate project SDLC deliverables and artifact using the project rubric.
  - Apply attendance gate and finalize grades.

## 9) Notes for Iteration

This draft intentionally optimizes simplicity and operational consistency.

Likely refinements after first review:

- exact number of homework submissions to count
- late-work and make-up exam policy
- minimum project requirements and milestone dates
- participation script rules for handling edge cases