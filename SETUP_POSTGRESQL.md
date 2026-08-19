# CashFlow Digital Twin - Complete PostgreSQL Setup

## Local Windows + PostgreSQL 18

PostgreSQL service:
`postgresql-x64-18`

Check:
```cmd
sc query postgresql-x64-18
```

It should say:
`STATE : 4 RUNNING`

Check client:
```cmd
"C:\Program Files\PostgreSQL\18\bin\psql.exe" --version
```

Connect:
```cmd
"C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -h localhost -p 5432
```

Create DB:
```sql
CREATE DATABASE cashflow_db;
\q
```

## Backend

```powershell
cd D:\Fintwin\backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env`:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=cashflow_db
DB_USER=postgres
DB_PASSWORD=YOUR_POSTGRES_PASSWORD
DB_HOST=localhost
DB_PORT=5432
```

Then:

```powershell
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Health:
`http://127.0.0.1:8000/health/`

Admin:
`http://127.0.0.1:8000/admin/`

## Important

Do not create a Python/Django app named `collections`; the project uses
`collections_app` because `collections` is a Python standard-library module.
