import axiosClient from './axiosClient'

export async function getRiskFlags() {
  const response = await axiosClient.get('/analytics/risk/')
  return response.data
}

export async function getSavingsAdvice() {
  const response = await axiosClient.get('/analytics/savings/')
  return response.data
}

export async function getSurvivability() {
  const response = await axiosClient.get('/analytics/survivability/')
  return response.data
}

export async function getRecoveryPlan() {
  const response = await axiosClient.get('/analytics/recovery-plan/')
  return response.data
}

export async function getShockPresets() {
  const response = await axiosClient.get('/analytics/simulate/presets/')
  return response.data
}

export async function runSimulation(shockId) {
  const response = await axiosClient.post('/analytics/simulate/', { shockId })
  return response.data?.series || []
}
