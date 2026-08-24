import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import SectionHeader from '../components/common/SectionHeader'
import { register as registerApi, login as loginApi } from '../api/authApi'
import { useAuth } from '../context/AuthContext'

export default function RegisterPage() {
  const [form, setForm] = useState({ username: '', email: '', password: '', business_name: '' })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const { login } = useAuth()
  const navigate = useNavigate()

  const submit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')
    try {
      await registerApi(form)
      const tokens = await loginApi(form.username, form.password)
      login(form.username, tokens.access, tokens.refresh, { businessName: form.business_name })
      navigate('/onboarding')
    } catch (err) {
      setError(err.response?.data ? JSON.stringify(err.response.data) : 'Registration failed.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-md mx-auto px-6 py-10">
      <SectionHeader eyebrow="Create account" title="Set up your business" subtitle="Your financial data stays behind the consent and correction workflow." />
      <form onSubmit={submit} className="ledger-card p-6 space-y-4">
        {['username', 'email', 'business_name', 'password'].map((field) => (
          <label key={field} className="block">
            <span className="text-[11px] font-mono uppercase text-muted">{field.replace('_', ' ')}</span>
            <input type={field === 'password' ? 'password' : field === 'email' ? 'email' : 'text'} required value={form[field]} onChange={(e) => setForm({ ...form, [field]: e.target.value })} className="mt-1 w-full rounded-md border border-charcoal/15 px-3 py-2 text-sm" />
          </label>
        ))}
        {error && <p className="text-xs text-stamp break-words">{error}</p>}
        <button disabled={loading} className="w-full py-2.5 rounded-md bg-ink text-paper text-sm font-medium disabled:opacity-50">{loading ? 'Creating…' : 'Create account'}</button>
        <p className="text-xs text-center text-muted">Already registered? <Link className="text-ink underline" to="/login">Sign in</Link></p>
      </form>
    </div>
  )
}
