$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$backend = Join-Path $root 'backend'
$frontend = Join-Path $root 'frontend'
$venv = Join-Path $backend '.venv'
$python = Join-Path $venv 'Scripts\python.exe'
$envFile = Join-Path $backend '.env'

Write-Host ''
Write-Host '=========================================' -ForegroundColor Cyan
Write-Host ' Fintwin - Windows Setup' -ForegroundColor Cyan
Write-Host '=========================================' -ForegroundColor Cyan
Write-Host "Project: $root"

# Find a usable Python launcher.
$pythonLauncher = $null
if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonLauncher = 'py'
    $pythonArgs = @('-3')
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonLauncher = 'python'
    $pythonArgs = @()
} else {
    throw 'Python was not found. Install Python 3.12+ and make sure python.exe is on PATH.'
}

if (-not (Test-Path $venv)) {
    Write-Host 'Creating Python virtual environment...' -ForegroundColor Yellow
    & $pythonLauncher @pythonArgs -m venv $venv
}

if (-not (Test-Path $python)) {
    throw "Virtual environment was not created correctly: $python"
}

Write-Host 'Installing backend dependencies...' -ForegroundColor Yellow
& $python -m pip install --upgrade pip
& $python -m pip install -r (Join-Path $backend 'requirements.txt')

# Locate psql. PostgreSQL's normal bin path is checked first, then pgAdmin runtime.
$psqlCandidates = @(
    'C:\Program Files\PostgreSQL\18\bin\psql.exe',
    'C:\Program Files\PostgreSQL\17\bin\psql.exe',
    'C:\Program Files\PostgreSQL\16\bin\psql.exe',
    'C:\Program Files\PostgreSQL\15\bin\psql.exe',
    'C:\Program Files\PostgreSQL\14\bin\psql.exe',
    'C:\Program Files\PostgreSQL\18\pgAdmin 4\runtime\psql.exe'
)
$psql = $psqlCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $psql) {
    throw 'psql.exe was not found. Install PostgreSQL command-line tools or update SETUP_WINDOWS.ps1 with your psql.exe path.'
}

Write-Host "Using psql: $psql" -ForegroundColor Green

$dbPassword = Read-Host "Enter the PostgreSQL password for user 'postgres'"
if ([string]::IsNullOrWhiteSpace($dbPassword)) {
    throw 'PostgreSQL password cannot be empty.'
}

# Verify credentials before writing .env or running migrations.
$oldPgPassword = $env:PGPASSWORD
try {
    $env:PGPASSWORD = $dbPassword
    & $psql -h 127.0.0.1 -p 5432 -U postgres -d cashflow_db -c 'SELECT 1;' | Out-Host
    if ($LASTEXITCODE -ne 0) {
        throw 'PostgreSQL authentication failed. The password entered is not the password for postgres, or PostgreSQL is not accepting TCP connections on 127.0.0.1:5432.'
    }
} finally {
    $env:PGPASSWORD = $oldPgPassword
}

$envLines = @(
    'DJANGO_SECRET_KEY=dev-change-this'
    'DEBUG=True'
    'ALLOWED_HOSTS=127.0.0.1,localhost'
    'CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173'
    'DB_ENGINE=django.db.backends.postgresql'
    'DB_NAME=cashflow_db'
    'DB_USER=postgres'
    "DB_PASSWORD=$dbPassword"
    'DB_HOST=127.0.0.1'
    'DB_PORT=5432'
    'CELERY_BROKER_URL=redis://127.0.0.1:6379/0'
    'CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/0'
    'CELERY_TASK_ALWAYS_EAGER=True'
)
$envLines | Set-Content -Path $envFile -Encoding UTF8

Set-Location $backend
Write-Host 'Checking Django...' -ForegroundColor Yellow
& $python manage.py check

Write-Host 'Running migrations...' -ForegroundColor Yellow
& $python manage.py migrate

Write-Host 'Loading demo data...' -ForegroundColor Yellow
& $python manage.py seed_demo

Write-Host ''
Write-Host 'Backend setup complete.' -ForegroundColor Green
Write-Host 'Demo login: demo / Demo@12345' -ForegroundColor Green
Write-Host ''
Write-Host 'Next:' -ForegroundColor Cyan
Write-Host '  Backend:  cd backend; .venv\Scripts\Activate.ps1; python manage.py runserver'
Write-Host '  Frontend: cd frontend; npm install; npm run dev'
Write-Host '  Browser:  http://localhost:5173'
