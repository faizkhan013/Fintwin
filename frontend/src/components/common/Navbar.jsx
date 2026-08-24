import React from 'react'
import { NavLink, useNavigate } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'

const links = [
  { to: '/dashboard', label: 'Ledger' },
  { to: '/upload', label: 'Import' },
  { to: '/simulation', label: 'Simulate' },
  { to: '/financing', label: 'Financing' },
  { to: '/collections', label: 'Collections' },
  { to: '/market', label: 'Market' },
]

export default function Navbar() {
  const { user, logout, isAuthenticated } = useAuth()
  const navigate = useNavigate()

  if (!isAuthenticated) return null

  return (
    <header className="border-b border-charcoal/10 bg-paper/95 backdrop-blur sticky top-0 z-30">
      <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <div className="flex items-baseline gap-1">
          <span className="font-display text-xl font-semibold tracking-tight">Khata</span>
          <span className="font-display text-xl italic text-brass">Twin</span>
        </div>
        <nav className="hidden md:flex items-center gap-1">
          {links.map((l) => (
            <NavLink
              key={l.to}
              to={l.to}
              className={({ isActive }) =>
                `px-3 py-1.5 text-sm rounded-md transition-colors ${
                  isActive ? 'bg-ink text-paper' : 'text-charcoal/75 hover:bg-charcoal/5'
                }`
              }
            >
              {l.label}
            </NavLink>
          ))}
        </nav>
        <div className="flex items-center gap-3">
          <span className="text-sm text-muted hidden sm:inline">{user?.businessName}</span>
          <button
            onClick={() => { logout(); navigate('/login') }}
            className="text-sm font-medium px-3 py-1.5 rounded-md border border-charcoal/15 hover:bg-charcoal/5"
          >
            Sign out
          </button>
        </div>
      </div>
    </header>
  )
}
