# DevBridge

**Project-Based Developer Assessment and Professional Opportunity Platform**

DevBridge connects developers—especially university students and early-career programmers—with companies through practical software projects. Companies can publish structured projects, assess submissions against their own marking criteria, and identify capable developers through demonstrated work.

## Product overview

- **Demo projects:** Free and unpaid projects published by companies with marking rubrics. Developers submit work through a GitHub URL or ZIP and receive AI-assisted assessment and feedback.
- **Live projects:** Opportunities published by verified companies. Only developers with an active paid Premium subscription can apply. Companies select, supervise and evaluate developers. Compensation (paid or unpaid) must be stated clearly.
- **Performance and ranking:** Based on factors such as quality, difficulty, success rate, consistency, deadlines and company evaluation. Exact weights are still being decided.
- **Premium:** Eligibility and paid subscription are separate; meeting an eligibility pathway does not automatically activate Premium.

## Project principles

- Assess practical work, not just CVs.
- Companies define the criteria used to assess their demo projects.
- Keep evidence and explanations alongside AI-assisted assessment.
- Do not claim code was executed or tested unless it really was.
- Keep API secrets and database credentials out of source control.
- Enforce roles, ownership, verification and Premium access in the backend; hiding a frontend control is not authorization.
- Both project members contribute across frontend, backend, database, integration and testing through full-stack module ownership.

## Technology stack

| Layer | Technology |
|---|---|
| Web and mobile client | Expo, React Native, TypeScript, Expo Router |
| Backend API | Python, FastAPI |
| Database | PostgreSQL |
| ORM and migrations | SQLAlchemy, Alembic |
| Authentication support | pwdlib / Argon2, PyJWT |
| API style | REST over HTTPS (planned production configuration) |

## Architecture and team workflow

The project is developed by two people using **full-stack, module-based ownership**. We do not divide the work into a frontend person and a backend person. Each person owns complete functional modules, including UI/UX, frontend, backend, database/SQL, APIs, tests and documentation.

Development is incremental (Sprints 0–8): shared foundation first, then independently developed modules with planned integration checkpoints. Architecture, common contracts, security reviews, integration and final release are joint responsibilities.

See [System Architecture and Development Plan](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/SYSTEM_ARCHITECTURE.md) for architecture, data flows, functional modules, responsibility allocation, sprint plan, Git/testing conventions and open decisions.

## Database design direction

The complete platform schema is still being designed. The initial database contains five core tables; the complete domain model is not yet implemented.

Agreed conceptual directions include:
- A shared project model for DEMO and LIVE projects, with type-specific workflows handled through related records.
- A project can belong to multiple categories through a many-to-many relationship.
- A shared skills and technologies catalogue is reused by developer profiles and project requirements.
- Project skill requirements distinguish required and preferred skills.

These are **design decisions, not implemented project-domain tables**. See the [Database Design](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/DATABASE_DESIGN.md) document for details and remaining decisions.

## Repository structure

```text
DevBridge/
├── backend/       # FastAPI application, models and migrations
├── frontend/      # Expo / React Native / TypeScript application
├── database/      # Database-related scripts and design assets
├── docs/          # Application documentation
└── README.md
```

## Current implementation status

The repository contains the initial frontend and backend foundations, PostgreSQL connection/session setup, five core database models and an applied initial Alembic migration. Authentication libraries have been installed and smoke-tested, but registration/login workflows are not yet implemented.

The five current tables are:
- `users`
- `developer_profiles`
- `company_profiles`
- `student_verifications`
- `email_verifications`

Do not treat a planned feature as working software. Check the [Current Implementation Progress](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/CURRENT_PROGRESS.md) document before assuming a capability exists.

## Documentation repository

The application source code is maintained in this repository. The detailed project documentation is maintained separately in [Wathsalya180/DevBridge_chat](https://github.com/Wathsalya180/DevBridge_chat).

Useful documentation:
1. [Documentation repository README](https://github.com/Wathsalya180/DevBridge_chat/blob/main/README.md)
2. [Project overview](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/PROJECT_OVERVIEW.md)
3. [Software requirements specification](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/SRS.md)
4. [System architecture](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/SYSTEM_ARCHITECTURE.md)
5. [User roles and workflows](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/USER_ROLES_AND_WORKFLOWS.md)
6. [Business rules](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/BUSINESS_RULES.md)
7. [Database design](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/DATABASE_DESIGN.md)
8. [API documentation](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/API_DOCUMENTATION.md)
9. [Development setup](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/DEVELOPMENT_SETUP.md)
10. [Team workflow and module ownership](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/TEAM_WORKFLOW.md)
11. [Project roadmap](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/PROJECT_ROADMAP.md)
12. [Current implementation progress](https://github.com/Wathsalya180/DevBridge_chat/blob/main/docs/CURRENT_PROGRESS.md)

Documentation uses these status labels:
- **Implemented** — exists in the current codebase and has been checked.
- **Planned** — agreed direction, not necessarily implemented.
- **Proposed** — recommendation that still needs team approval.
- **TBD** — decision has not yet been made.

## Local development

### Backend

1. Open a terminal in `backend/`.
2. Activate the local virtual environment.
3. Install dependencies from `requirements.txt`.
4. Configure local database settings in `backend/.env` (never commit this file).
5. Start the API:

```powershell
python -m uvicorn app.main:app --reload
```

### Frontend

1. Open a terminal in `frontend/`.
2. Install dependencies with `npm install` if needed.
3. Start Expo:

```powershell
npx expo start
```

For web development:

```powershell
npx expo start --web
```
