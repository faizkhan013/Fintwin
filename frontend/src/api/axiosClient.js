import axios from 'axios'

const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api'

const axiosClient = axios.create({
  baseURL: BASE_URL,
  timeout: 20000,
  headers: { Accept: 'application/json' },
})

axiosClient.interceptors.request.use((config) => {
  const raw = sessionStorage.getItem('cft_user')
  if (raw) {
    try {
      const { token } = JSON.parse(raw)
      if (token) config.headers.Authorization = `Bearer ${token}`
    } catch {
      sessionStorage.removeItem('cft_user')
    }
  }
  return config
})

axiosClient.interceptors.response.use(
  (res) => res,
  (err) => {
    if (err.response?.status === 401) {
      sessionStorage.removeItem('cft_user')
      window.dispatchEvent(new Event('auth:expired'))
    }
    return Promise.reject(err)
  }
)

export function unwrapList(data) {
  return Array.isArray(data) ? data : (data?.results || [])
}

export default axiosClient
