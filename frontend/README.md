# KhataTwin — Cash-Flow Digital Twin (Frontend)

React (JS) + Vite frontend for the consent-based MSME cash-flow digital twin.

## Run locally
```
npm install
npm run dev
```

App runs on http://localhost:5173. Login accepts any email/password (demo auth).

## Backend
All API calls live in `src/api/*.js`. Each function currently returns mock data
(see `src/api/mockData.js`) with a small simulated delay, and has the real
Django/DRF axios call commented directly above it — swap the mock line for the
real call once the backend endpoints exist. Set `VITE_API_BASE_URL` in `.env`
to point at your Django server.

## Design
Ledger/ledger-book visual language (deep bottle-green ink, aged paper, brass
dividers, rubber-stamp red) built around one signature element: the "WHY"
explain-stamp attached to every risk flag and recommendation, which expands
to show the plain-English reasoning and the numbers behind it — this is the
UI's answer to the "explain every recommendation" requirement.

## Pages
Login → Onboarding (consent) → Upload → Correction (review OCR) → Dashboard
→ Simulation → Financing → Collections → Market (optional).
