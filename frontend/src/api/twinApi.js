import axiosClient from './axiosClient'

export async function getBalanceSeries() {
  const response = await axiosClient.get('/twin/balance-series/')
  return response.data
}

export async function getSummary() {
  const response = await axiosClient.get('/twin/summary/')
  return response.data
}

export async function getInvoices() {
  const response = await axiosClient.get('/twin/invoices/')
  return response.data
}

export async function rebuildTwin() {
  const response = await axiosClient.post('/twin/rebuild/')
  return response.data
}
