$ErrorActionPreference = 'Stop'
Set-Location (Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) 'backend')
& '.\.venv\Scripts\Activate.ps1'
python manage.py runserver
