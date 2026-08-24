import axiosClient from './axiosClient'

export async function logPartialPayment(invoiceId, amount) {
  const response = await axiosClient.post('/collections/partial-payment/', {
    invoice: invoiceId,
    amount,
    payment_date: new Date().toISOString().slice(0, 10),
  })
  return response.data
}

export async function flagForFollowUp(invoiceId, note) {
  const response = await axiosClient.post('/collections/follow-up/', {
    invoice: invoiceId,
    action_type: 'call',
    notes: note,
  })
  return response.data
}
