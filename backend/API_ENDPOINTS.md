# Fintwin API endpoints

All protected endpoints use `Authorization: Bearer <access_token>`.

## Authentication

- `POST /api/auth/token/` — obtain JWT access/refresh tokens
- `POST /api/auth/token/refresh/` — refresh access token
- `POST /api/accounts/register/` — create user + business profile
- `GET/PATCH /api/accounts/profile/` — current business profile

## Consent

- `GET /api/consent/` — list current user's consents
- `POST /api/consent/` — grant/update consent (`consent_type`, `purpose`, `duration_days`)
- `POST /api/consent/<id>/revoke/` — revoke consent

## Imports

- `POST /api/imports/upload/` — upload PDF/image/CSV/JSON
- `GET /api/imports/pending/` — extracted imports waiting for review
- `GET /api/imports/invoices/` — current user's invoices
- `POST /api/imports/<id>/confirm/` — confirm/correct an extracted import
- `PATCH /api/imports/invoice/<id>/` — update a single invoice

## Digital twin

- `GET /api/twin/` — current twin
- `POST /api/twin/entry/` — add a manual cash-flow entry
- `POST /api/twin/rebuild/` — rebuild twin + forecast + risks
- `GET /api/twin/summary/` — dashboard summary
- `GET /api/twin/balance-series/` — forecast chart data
- `GET /api/twin/invoices/` — receivables timeline

## Analytics

- `GET /api/analytics/forecast/` — 90-day hybrid ML forecast
- `GET /api/analytics/risk/` — explainable risk flags
- `GET /api/analytics/savings/` — emergency-savings planning advice
- `GET /api/analytics/survivability/` — cash-reserve survivability estimate
- `GET /api/analytics/recovery-plan/` — receivables recovery steps
- `GET /api/analytics/simulate/presets/` — supported shock presets
- `POST /api/analytics/simulate/` — run a shock simulation
- `GET /api/analytics/loans/` — illustrative lender-rate comparison
- `POST /api/analytics/financing/` — financing-option comparison
- `POST /api/analytics/opportunity-cost/` — financing vs waiting-cost comparison

## Collections

- `POST /api/collections/partial-payment/` — record a partial payment
- `POST /api/collections/follow-up/` — record a collection follow-up
- `GET /api/collections/actions/` — list collection actions

## Optional market analysis

- `GET /api/market/compare/?product=<name>&price=<amount>`
- `GET /api/market/references/`
- `POST /api/market/references/` — admin only
