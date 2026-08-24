import axiosClient, { unwrapList } from './axiosClient'

const typeMap = {
  Invoices: 'invoice',
  'Payment history': 'payment',
  'Recurring expenses': 'expense',
  Receivables: 'receivable',
  'Bank data': 'bank',
}
const labelMap = Object.fromEntries(Object.entries(typeMap).map(([label, value]) => [value, label]))

function normalize(c) {
  return {
    ...c,
    dataType: labelMap[c.consent_type] || c.data_type || c.consent_type,
    status: c.status || (c.granted ? 'active' : 'revoked'),
    expiresAt: c.expires_at,
  }
}

export async function getConsents() {
  const response = await axiosClient.get('/consent/')
  return unwrapList(response.data).map(normalize)
}

export async function grantConsent(dataType, purpose, durationDays = 90) {
  const response = await axiosClient.post('/consent/', {
    consent_type: typeMap[dataType] || dataType,
    purpose,
    duration_days: durationDays,
  })
  return normalize(response.data)
}

export async function revokeConsent(id) {
  const response = await axiosClient.post(`/consent/${id}/revoke/`)
  return normalize(response.data)
}
