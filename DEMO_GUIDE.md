# KhataTwin Demo Guide

## 1. PostgreSQL
Create a database named `cashflow_db` and make sure PostgreSQL 18 is running on port 5432.

## 2. Backend
From PowerShell at the project root:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\SETUP_WINDOWS.ps1
```

The script creates `backend/.env` using the PostgreSQL password you enter, runs migrations, and seeds a demo account.

Then:

```powershell
cd backend
.venv\Scripts\Activate.ps1
python manage.py runserver
```

Verify:

- `http://127.0.0.1:8000/health/`
- `http://127.0.0.1:8000/health/db/`

The second endpoint confirms Django can actually query PostgreSQL.

## 3. Frontend
In a second PowerShell:

```powershell
cd frontend
npm install
npm run dev
```

Open the Vite URL, normally `http://localhost:5173`.

## 4. Demo login

```text
Username: demo
Password: Demo@12345
```

The demo user already has:

- consent records
- approved invoices
- partial payment history
- expenses
- historical cash movements
- 90-day forecast
- risk metrics
- market price references

## 5. Demo flow

1. Sign in.
2. Review the consent screen.
3. Open **Ledger** to show the digital twin.
4. Open **Collections** and log a partial payment.
5. Open **Simulate** and run a shock scenario.
6. Open **Financing** to compare options.
7. Open **Market** and search `Cotton bedsheet set (queen)`.
8. Upload an invoice/CSV to demonstrate the OCR/import/correction workflow.

## Architecture

React + JavaScript → Django REST Framework → PostgreSQL

Celery/Redis are optional for the demo because development uses eager task execution by default.
