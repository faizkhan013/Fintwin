import axiosClient from './axiosClient'

export async function login(username, password) {
  const response = await axiosClient.post('/auth/token/', { username, password })
  return response.data
}

export async function refreshToken(refresh) {
  const response = await axiosClient.post('/auth/token/refresh/', { refresh })
  return response.data
}

export async function register(payload) {
  const response = await axiosClient.post('/accounts/register/', payload)
  return response.data
}

export async function getProfile() {
  const response = await axiosClient.get('/accounts/profile/')
  return response.data
}
