# Fintwin Backend

Django 5 + Django REST Framework backend for the Cash-Flow Digital Twin.

## Apps

- `accounts` — JWT-authenticated users and business profiles
- `consent` — purpose-bound consent with expiry/revocation
- `imports` — invoice/file upload, OCR/parser and correction queue
- `digital_twin` — cash-flow twin, entries and forecast storage
- `analytics` — ML forecast, explainable risk, simulation and financing comparison
- `collections_app` — partial payments and collection actions
- `market_analysis` — optional price-reference comparison
- `audit` — authenticated request audit trail

## Run

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env   # Windows
# cp .env.example .env   # Linux/macOS
python manage.py migrate
python manage.py runserver
```

For PostgreSQL, set the database variables in `.env`. The project is configured for PostgreSQL by default.

Celery/Redis are optional for local development because `CELERY_TASK_ALWAYS_EAGER=True` in the development example. Set it to `False` when running a real Celery worker.
