import React, { createContext, useContext, useState, useCallback, useEffect } from 'react'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const raw = sessionStorage.getItem('cft_user')
    try { return raw ? JSON.parse(raw) : null } catch { return null }
  })

  const login = useCallback((username, token, refresh = null, profile = null) => {
    const nextUser = { username, token, refresh, ...(profile || {}) }
    sessionStorage.setItem('cft_user', JSON.stringify(nextUser))
    setUser(nextUser)
  }, [])

  const updateProfile = useCallback((profile) => {
    setUser((current) => {
      const next = { ...(current || {}), ...profile }
      sessionStorage.setItem('cft_user', JSON.stringify(next))
      return next
    })
  }, [])

  const logout = useCallback(() => {
    sessionStorage.removeItem('cft_user')
    setUser(null)
  }, [])

  useEffect(() => {
    const handler = () => logout()
    window.addEventListener('auth:expired', handler)
    return () => window.removeEventListener('auth:expired', handler)
  }, [logout])

  return <AuthContext.Provider value={{ user, login, logout, updateProfile, isAuthenticated: !!user?.token }}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
