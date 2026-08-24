import axios from 'axios'

const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api'

const axiosClient = axios.create({
  baseURL: BASE_URL,
  headers: { 'Content-Type': 'application/json' },
})

axiosClient.interceptors.request.use((config) => {
  const raw = sessionStorage.getItem('cft_user')
  if (raw) {
    const { token } = JSON.parse(raw)
    if (token) config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

axiosClient.interceptors.response.use(
  (res) => res,
  (err) => {
    if (err.response?.status === 401) {
      sessionStorage.removeItem('cft_user')
    }
    return Promise.reject(err)
  }
)

// Simulated network delay so loading states are visible while the
// real Django endpoints aren't wired up yet.
export function mockDelay(data, ms = 450) {
  return new Promise((resolve) => setTimeout(() => resolve(data), ms))
}

export default axiosClient
