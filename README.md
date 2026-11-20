# DevBridge

**Project-Based Developer Assessment and Professional Opportunity Platform**

DevBridge connects developers/students with companies through structured demo projects and professional live-project opportunities.

## Product overview

- **Demo projects:** free and unpaid projects published by companies with marking rubrics. Developers submit work through a GitHub URL or ZIP and receive AI-assisted assessment and feedback.
- **Live projects:** opportunities published by verified companies. Only developers with an active paid Premium subscription can apply. Companies select, supervise and evaluate developers. Compensation (paid or unpaid) must be stated clearly.
- **Performance and ranking:** based on factors such as quality, difficulty, success rate, consistency, deadlines and company evaluation. Exact weights are still being decided.
- **Premium:** eligibility and paid subscription are separate; meeting an eligibility pathway does not automatically activate Premium.

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

See [System Architecture and Development Plan](docs/SYSTEM_ARCHITECTURE.md) for the architecture, data flows, functional modules, responsibility allocation, Sprint 0–8 plan, Git/testing conventions and open decisions.

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

The five current tables are only the initial shared database core. The complete platform database design and ER diagram are part of the common foundation milestone.

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
