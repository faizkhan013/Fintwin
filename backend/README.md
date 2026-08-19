# CashFlow Digital Twin - Backend

Django + Django REST Framework backend for SOAIDEATHON-S42.

## Features

- JWT authentication
- MSME business profile
- Explicit consent management
- Invoice/PDF/image import pipeline
- User correction/review workflow
- Cash-flow digital twin
- 90-day forecast
- Delayed-payment and customer-concentration risk
- Shock simulation
- Financing/loan comparison
- Opportunity-cost analysis
- Emergency savings guidance
- Recovery plan
- Partial payments and collection actions
- Optional market-price comparison
- Audit logging
- Celery + Redis background jobs
- PostgreSQL support

## Run locally

### 1. Create environment

Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

For quick development without PostgreSQL, edit `.env`:

```env
DB_ENGINE=django.db.backends.sqlite3
```

### 2. Migrate

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 3. Start API

```bash
python manage.py runserver
```

### 4. Optional Celery

Start Redis, then:

```bash
celery -A config worker -l info
```

## JWT

POST `/api/auth/token/`:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Use:

`Authorization: Bearer <access_token>`

## Important product rule

This backend is an advisory financial-planning system. It does **not** make automatic lending decisions or approve/reject loans. Financing comparisons return modeled costs and explanations so the MSME user can decide.

The bank rate JSON is illustrative seed data and must not be presented as live bank offers.
