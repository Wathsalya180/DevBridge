# DevBridge

**A Project-Based Developer Assessment and Professional Opportunity Platform**

DevBridge is a web and mobile platform designed to connect software developers—especially university students and early-career programmers—with companies through practical software projects.

The central idea is simple: **demonstrate skills through real work, not only through a CV.**

## The problem DevBridge addresses

Students and early-career developers may understand programming concepts but have limited opportunities to demonstrate their abilities through realistic tasks. At the same time, companies may find it difficult to assess a candidate's practical skills using a CV alone.

DevBridge aims to bridge this gap by providing structured projects, transparent assessment criteria, feedback and a pathway from practice to professional opportunities.

## Who uses DevBridge?

- **Developers:** Build practical experience, submit project work, receive structured feedback, build a record of performance and apply for eligible live projects.
- **Companies:** Publish project briefs, define assessment criteria, review submissions and identify capable developers through demonstrated work.
- **Administrators:** Verify companies, oversee platform activity and manage safety, moderation and platform rules.

## How the platform works

### 1. Demo projects

Demo projects are free, unpaid practice and assessment opportunities.

- Companies publish a project brief and define its marking rubric.
- Developers discover projects and submit their work through a GitHub repository URL or ZIP file.
- The planned AI-assisted assessment reviews submitted code and documentation against the company's criteria and provides scores, evidence and feedback.
- Demo projects help developers build experience and a history of assessed work.

The initial assessment approach is static inspection; the platform must not claim that submitted code was executed or tested unless a separate secure execution system is actually implemented.

### 2. Performance and Premium

Developers build a performance history through their completed project work. Performance and ranking are intended to consider factors such as solution quality, project difficulty, success rate, consistency, deadlines and company evaluations. Exact ranking weights remain under design.

Premium has two separate concepts:

- **Eligibility:** A developer must meet an approved performance pathway.
- **Subscription:** The developer must separately purchase and maintain an active paid Premium subscription.

Meeting the eligibility requirements does not automatically activate Premium.

### 3. Live projects

Live projects are real-world opportunities published by verified companies.

- Only verified companies may publish live projects.
- Developers need an active paid Premium subscription to apply.
- Companies review applications, select developers, supervise the work and provide evaluations.
- Each listing must clearly state whether the project is paid or unpaid and explain its compensation terms.
- Premium access does not guarantee selection or payment.

## Product direction

DevBridge is intended to support **both web and mobile**. Development is currently web-first while using Expo, React Native and TypeScript to share application code where practical.

## Project principles

- Assess practical work, not just CVs.
- Make assessment criteria and feedback understandable.
- Keep evidence and explanations alongside AI-assisted assessment.
- Do not claim code was executed or tested unless it really was.
- Protect user data and keep API secrets and database credentials out of source control.
- Enforce roles, ownership, company verification and Premium access in the backend; hiding a frontend control is not authorization.
- Distinguish Premium eligibility from an active paid subscription.

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

Development is incremental: the shared foundation is established first, followed by independently developed modules and planned integration checkpoints. Architecture, common contracts, security reviews, integration and final release are joint responsibilities.

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

The repository contains the initial frontend and backend foundations, PostgreSQL connection/session setup, five core database models and an applied initial Alembic migration. Authentication libraries have been installed and smoke-tested, but registration and login workflows are not yet implemented.

The five current database tables are:

- `users`
- `developer_profiles`
- `company_profiles`
- `student_verifications`
- `email_verifications`

The complete project, submission, evaluation, Premium and live-project feature sets are still being designed and developed. Do not treat a planned feature as working software.

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
