# Fintwin Frontend

React 18 + JavaScript + Vite frontend for the consent-based MSME cash-flow digital twin.

## Run locally

```bash
npm install
npm run dev
```

App: `http://localhost:5173`

Set `VITE_API_BASE_URL` in `.env` to the Django API, for example:

```text
VITE_API_BASE_URL=http://localhost:8000/api
```

## API integration

All API calls are in `src/api/*.js` and use Axios. The frontend is connected to the real Django endpoints; there is no mock-data fallback.

## Pages

Login/Register → Onboarding/Consent → Upload → OCR Correction → Dashboard → Simulation → Financing → Collections → Market Analysis.
