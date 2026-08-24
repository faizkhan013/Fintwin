import axiosClient, { mockDelay } from './axiosClient'

export async function logPartialPayment(invoiceId, amount) {
  // Real call: return (await axiosClient.post('/collections/partial-payment/', { invoiceId, amount })).data
  return mockDelay({ ok: true, invoiceId, amount })
}

export async function flagForFollowUp(invoiceId, note) {
  // Real call: return (await axiosClient.post('/collections/follow-up/', { invoiceId, note })).data
  return mockDelay({ ok: true, invoiceId, note })
}
