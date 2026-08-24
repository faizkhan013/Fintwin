import axiosClient, { mockDelay } from './axiosClient'

export async function getConsents() {
  // Real call: return (await axiosClient.get('/consent/')).data
  return mockDelay([
    { id: 1, dataType: 'Invoices', purpose: 'Cash-flow forecasting', status: 'active', expiresAt: '2026-11-18' },
    { id: 2, dataType: 'Payment history', purpose: 'Risk & delay analysis', status: 'active', expiresAt: '2026-11-18' },
    { id: 3, dataType: 'Recurring expenses', purpose: 'Liquidity forecasting', status: 'active', expiresAt: '2026-11-18' },
  ])
}

export async function grantConsent(dataType, purpose, durationDays) {
  // Real call: return (await axiosClient.post('/consent/', { dataType, purpose, durationDays })).data
  return mockDelay({ ok: true, dataType, purpose, durationDays })
}

export async function revokeConsent(id) {
  // Real call: return (await axiosClient.post(`/consent/${id}/revoke/`)).data
  return mockDelay({ ok: true })
}
