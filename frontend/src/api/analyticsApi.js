import axiosClient, { mockDelay } from './axiosClient'
import {
  mockRiskFlags, mockSavingsAdvice, mockSurvivability,
  mockRecoverySteps, mockShockPresets, mockBalanceSeries,
} from './mockData'

export async function getRiskFlags() {
  // Real call: return (await axiosClient.get('/analytics/risk/')).data
  return mockDelay(mockRiskFlags)
}

export async function getSavingsAdvice() {
  // Real call: return (await axiosClient.get('/analytics/savings/')).data
  return mockDelay(mockSavingsAdvice)
}

export async function getSurvivability() {
  // Real call: return (await axiosClient.get('/analytics/survivability/')).data
  return mockDelay(mockSurvivability)
}

export async function getRecoveryPlan() {
  // Real call: return (await axiosClient.get('/analytics/recovery-plan/')).data
  return mockDelay(mockRecoverySteps)
}

export async function getShockPresets() {
  // Real call: return (await axiosClient.get('/analytics/simulate/presets/')).data
  return mockDelay(mockShockPresets)
}

export async function runSimulation(shockId) {
  // Real call: return (await axiosClient.post('/analytics/simulate/', { shockId })).data
  const shocked = mockBalanceSeries.map((pt, i) => {
    if (pt.projected == null) return pt
    const penalty = shockId === 'lost_customer' ? 34000 : shockId === 'expense_spike' ? 18000 : 22000
    return { ...pt, shocked: i >= 3 ? pt.projected - penalty : pt.projected }
  })
  return mockDelay(shocked, 700)
}
