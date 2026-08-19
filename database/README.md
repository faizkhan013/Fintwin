# PostgreSQL Database

Database name: `cashflow_db`

Default local connection:
- Host: `localhost`
- Port: `5432`
- User: `postgres`

## Recommended setup

1. Install PostgreSQL 18.
2. Make sure the `postgresql-x64-18` service is RUNNING.
3. Create the database:

```sql
CREATE DATABASE cashflow_db;
```

4. Configure `backend/.env`:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=cashflow_db
DB_USER=postgres
DB_PASSWORD=YOUR_POSTGRES_PASSWORD
DB_HOST=localhost
DB_PORT=5432
```

5. From `backend/`:

```powershell
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

The Django ORM is the source of truth for application schema. Do not run the optional
`schema.sql` against an already-migrated Django database because it is intended for
database inspection/bootstrap/reference.

## Docker

From the project root:

```powershell
docker compose up -d db redis
```

Then:

```powershell
cd backend
python manage.py migrate
```
