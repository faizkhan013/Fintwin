import axiosClient from './axiosClient'

export async function getBankRates(amount = 100000, months = 12) {
  const response = await axiosClient.get('/analytics/loans/', { params: { amount, months } })
  return response.data
}

export async function getFinancingComparison(requiredAmount = 100000, financingCost = 6, monthlyCashGap = 0) {
  const response = await axiosClient.post('/analytics/financing/', {
    required_amount: requiredAmount,
    financing_cost: financingCost,
    monthly_cash_gap: monthlyCashGap,
  })
  return response.data
}

export async function getOpportunityCost(data = {}) {
  const response = await axiosClient.post('/analytics/opportunity-cost/', data)
  return response.data
}
