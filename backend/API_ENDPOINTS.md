# API Endpoints

Base URL: `http://127.0.0.1:8000`

Authentication uses JWT. Protected requests use:

`Authorization: Bearer <access_token>`

| Endpoint | Method | Purpose |
|---|---|---|
| `/health/` | GET | Backend health |
| `/api/auth/token/` | POST | Login |
| `/api/auth/token/refresh/` | POST | Refresh token |
| `/api/accounts/register/` | POST | Register MSME user |
| `/api/accounts/profile/` | GET/PUT/PATCH | Business profile |
| `/api/consent/` | GET/POST | List/create consent |
| `/api/consent/{id}/revoke/` | PUT/PATCH | Revoke consent |
| `/api/imports/` | GET/POST | List/upload imports |
| `/api/imports/invoice/{id}/` | GET/PUT/PATCH | Review/correct invoice |
| `/api/imports/{id}/approve/` | PUT/PATCH | Approve imported data |
| `/api/twin/` | GET | Digital twin |
| `/api/twin/entry/` | POST | Add income/expense |
| `/api/twin/build/` | POST | Rebuild twin + forecast |
| `/api/collections/partial-payment/` | POST | Record partial payment |
| `/api/collections/action/` | POST | Log collection action |
| `/api/collections/actions/` | GET | Collection history |
| `/api/analytics/risk/` | GET | Risk summary |
| `/api/analytics/simulation/` | POST | Shock simulation |
| `/api/analytics/loans/` | GET | Illustrative loan comparison |
| `/api/analytics/financing/` | POST | Financing cost comparison |
| `/api/analytics/opportunity-cost/` | POST | Wait vs finance cost |
| `/api/analytics/savings/` | GET | Emergency savings guidance |
| `/api/analytics/recovery/` | POST | Recovery plan |
| `/api/market/compare/` | GET | Market price comparison |
| `/api/market/references/` | GET/POST | Price references; POST is admin-only |
