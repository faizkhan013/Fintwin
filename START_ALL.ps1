$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$backendScript = Join-Path $root 'START_BACKEND.ps1'
$frontendScript = Join-Path $root 'START_FRONTEND.ps1'

Start-Process powershell -ArgumentList '-NoExit', '-ExecutionPolicy', 'Bypass', '-File', $backendScript
Start-Sleep -Seconds 2
Start-Process powershell -ArgumentList '-NoExit', '-ExecutionPolicy', 'Bypass', '-File', $frontendScript
Write-Host 'Backend and frontend terminals started.' -ForegroundColor Green
Write-Host 'Open http://localhost:5173'
