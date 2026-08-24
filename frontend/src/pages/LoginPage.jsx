import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { login as loginApi } from '../api/authApi'

export default function LoginPage() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const { login } = useAuth()
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
  e.preventDefault()
  setLoading(true)

  try {
    const res = await loginApi(username, password)

    login(username, res.access)

    navigate('/dashboard')
  } catch (error) {
    console.error('Login failed:', error)
    alert('Invalid username or password')
  } finally {
    setLoading(false)
  }
}

  return (
    <div className="min-h-screen flex items-center justify-center bg-ledger px-4">
      <div className="ledger-card w-full max-w-sm p-8">
        <div className="mb-6 text-center">
          <p className="font-display text-2xl">
            Khata<span className="italic text-brass">Twin</span>
          </p>
          <p className="text-sm text-muted mt-1">Your cash-flow digital twin</p>
        </div>
        <form onSubmit={handleSubmit} className="space-y-4">
          <label className="block">
            <span className="text-[11px] font-mono uppercase text-muted">Username</span>
           <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="mt-1 w-full rounded-md border border-charcoal/15 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brass/50"
                 placeholder="Your username"
              />
          </label>
          <label className="block">
            <span className="text-[11px] font-mono uppercase text-muted">Password</span>
            <input
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="mt-1 w-full rounded-md border border-charcoal/15 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brass/50"
              placeholder="••••••••"
            />
          </label>
          <button
            type="submit"
            disabled={loading}
            className="w-full py-2.5 rounded-md bg-ink text-paper text-sm font-medium hover:bg-inkdeep disabled:opacity-50"
          >
            {loading ? 'Signing in…' : 'Sign in'}
          </button>
        </form>
      </div>
    </div>
  )
}
