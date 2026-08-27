# Fintwin — Cash-Flow Digital Twin

Fintwin is a consent-driven financial planning platform for micro and small enterprises. It turns approved invoices, receivables, payment information and cash-flow entries into a living cash-flow model, then provides explainable forecasting, risk flags, stress simulations and financing comparisons.

**Important:** Fintwin is a decision-support tool. It does not approve loans or make automatic lending decisions.

## Stack

- Frontend: React 18 + JavaScript, Vite, Tailwind CSS, Recharts, Axios
- Backend: Python 3.12+, Django 5, Django REST Framework, JWT
- Database: PostgreSQL 16+
- Background jobs: Celery + Redis
- OCR: Tesseract/PDFPlumber
- Analytics/ML: NumPy, Pandas, scikit-learn, explainable rule engine

## Architecture

```text
React + JavaScript
       |
       | REST / JSON
       v
Django REST Framework
       |
       +--> accounts      authentication + business profile
       +--> consent       consent guardrail
       +--> imports       upload + OCR + correction queue
       +--> digital_twin cash-flow model + forecast points
       +--> analytics     forecast + risk + simulation + financing
       +--> collections   partial payments + follow-up actions
       +--> market        optional price-reference tool
       +--> audit         request audit trail
       |
       v
PostgreSQL

Celery <--> Redis
```

## Project structure

```text
Fintwin/
├── frontend/                  # React + JavaScript
│   └── src/
│       ├── api/               # Axios API clients
│       ├── components/        # Reusable UI
│       ├── pages/             # Application screens
│       └── context/           # Authentication state
│
├── backend/                   # Django + DRF
│   ├── config/                # settings + root routes + Celery
│   ├── accounts/              # users/business profiles
│   ├── consent/               # consent lifecycle
│   ├── imports/               # files, OCR, invoice correction
│   ├── digital_twin/          # cash-flow twin + forecast storage
│   ├── analytics/              # forecasting, risk, simulation, financing
│   ├── collections_app/       # partial payments + follow-up
│   ├── market_analysis/       # optional market comparison
│   ├── audit/                 # audit logging
│   └── requirements.txt
│
├── database/                  # optional reference schema + seed data
├── docker-compose.postgres.yml
└── README.md
```

## Setup

### 1. PostgreSQL and Redis

The easiest option is Docker:

```bash
docker compose -f docker-compose.postgres.yml up -d
```

Or run PostgreSQL and Redis locally.

### 2. Backend

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Linux/macOS:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

Create `frontend/.env` from `.env.example` if required:

```text
VITE_API_BASE_URL=http://localhost:8000/api
```

Frontend: `http://localhost:5173`
Backend: `http://localhost:8000`
Admin: `http://localhost:8000/admin/`
Health: `http://localhost:8000/health/`

## API routes

```text
POST /api/auth/token/
POST /api/auth/token/refresh/
POST /api/accounts/register/
GET  /api/accounts/profile/

GET  /api/consent/
POST /api/consent/
POST /api/consent/<id>/revoke/

POST /api/imports/upload/
GET  /api/imports/pending/
GET  /api/imports/invoices/
POST /api/imports/<id>/confirm/

GET  /api/twin/
GET  /api/twin/summary/
GET  /api/twin/balance-series/
GET  /api/twin/invoices/
POST /api/twin/rebuild/

GET  /api/analytics/forecast/
GET  /api/analytics/risk/
GET  /api/analytics/savings/
GET  /api/analytics/survivability/
GET  /api/analytics/recovery-plan/
GET  /api/analytics/simulate/presets/
POST /api/analytics/simulate/
GET  /api/analytics/loans/
POST /api/analytics/financing/
POST /api/analytics/opportunity-cost/

POST /api/collections/partial-payment/
POST /api/collections/follow-up/
GET  /api/collections/actions/

GET  /api/market/compare/
GET  /api/market/references/
```

## Data flow

```text
User registers
   -> grants consent
   -> uploads invoice/CSV/JSON/PDF
   -> OCR/parser extracts fields
   -> user corrects extracted values
   -> import is approved
   -> Digital Twin rebuilds
   -> forecast + risk engines run
   -> user can stress-test scenarios
   -> financing options are compared
```

### Guardrails

1. Financial imports are scoped to the authenticated user.
2. Consent records have purpose, grant/revoke timestamps and expiry.
3. Imported OCR data enters a review state before approval.
4. Partial payments cannot exceed invoice outstanding amount.
5. Financing output is informational and returns `USER_DECIDES` semantics; it does not make a lending decision.
6. Audit middleware records authenticated API activity.

## AI / ML layer

The current forecasting engine uses a hybrid approach:

- scheduled receivables/expenses from the digital twin;
- baseline daily cash-flow rates;
- a small linear-regression model on available actual cash movements when enough history exists;
- deterministic fallback when there is insufficient history.

This is intentionally separated from the financial rules. The ML model predicts patterns; deterministic rules explain and guard decisions.

## Quick demo

For Windows, run `SETUP_WINDOWS.ps1` from the project root. It creates the backend environment, checks PostgreSQL, runs migrations and creates a ready demo account (`demo` / `Demo@12345`). See `DEMO_GUIDE.md`.

## Windows demo setup

1. Ensure PostgreSQL 18 is running and the database `cashflow_db` exists.
2. From the project root run:
   `Set-ExecutionPolicy -Scope Process Bypass`
   `./SETUP_WINDOWS.ps1`
3. Enter the real password for the PostgreSQL `postgres` user when prompted.
4. Start both applications with `./START_ALL.ps1`, or start them manually.
5. Open `http://localhost:5173`.
6. Demo login: `demo` / `Demo@12345`.

The setup script verifies PostgreSQL authentication before creating `backend/.env`, then runs Django migrations and seeds demo data. The frontend uses `frontend/.env` to call Django at `http://127.0.0.1:8000/api`.
