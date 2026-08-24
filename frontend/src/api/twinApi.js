import axiosClient, { mockDelay } from './axiosClient'
import { mockBalanceSeries, mockSummary, mockInvoices } from './mockData'

export async function getBalanceSeries() {
  // Real call: return (await axiosClient.get('/digital-twin/balance-series/')).data
  return mockDelay(mockBalanceSeries)
}

export async function getSummary() {
  // Real call: return (await axiosClient.get('/digital-twin/summary/')).data
  return mockDelay(mockSummary)
}

export async function getInvoices() {
  // Real call: return (await axiosClient.get('/imports/invoices/')).data
  return mockDelay(mockInvoices)
}

export async function rebuildTwin() {
  // Real call: return (await axiosClient.post('/digital-twin/rebuild/')).data
  return mockDelay({ ok: true })
}
