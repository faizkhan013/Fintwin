import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import SectionHeader from '../components/common/SectionHeader'
import { getConsents, grantConsent } from '../api/consentApi'

const dataTypes = [
  { key: 'Invoices', purpose: 'Cash-flow forecasting' },
  { key: 'Payment history', purpose: 'Risk & delay analysis' },
  { key: 'Recurring expenses', purpose: 'Liquidity forecasting' },
]

export default function OnboardingPage() {
  const [consents, setConsents] = useState([])
  const [granted, setGranted] = useState({})
  const navigate = useNavigate()

  useEffect(() => {
    getConsents().then(setConsents)
  }, [])

  const handleGrant = async (dt) => {
    await grantConsent(dt.key, dt.purpose, 90)
    setGranted((g) => ({ ...g, [dt.key]: true }))
  }

  const allGranted = dataTypes.every((dt) => granted[dt.key] || consents.some((c) => c.dataType === dt.key))

  return (
    <div className="max-w-2xl mx-auto px-6 py-10">
      <SectionHeader
        eyebrow="Step 1 of 1"
        title="What data can we use?"
        subtitle="Nothing is imported or analyzed until you explicitly consent to each data type, for a stated purpose and time period. You can revoke any of these later."
      />
      <div className="space-y-3">
        {dataTypes.map((dt) => {
          const isGranted = granted[dt.key] || consents.some((c) => c.dataType === dt.key)
          return (
            <div key={dt.key} className="ledger-card p-4 flex items-center justify-between">
              <div>
                <p className="text-sm font-medium">{dt.key}</p>
                <p className="text-xs text-muted">Purpose: {dt.purpose} · valid 90 days</p>
              </div>
              <button
                onClick={() => handleGrant(dt)}
                disabled={isGranted}
                className={`text-sm font-medium px-4 py-1.5 rounded-md ${
                  isGranted ? 'bg-verified/15 text-verified' : 'bg-ink text-paper hover:bg-inkdeep'
                }`}
              >
                {isGranted ? 'Granted' : 'Grant access'}
              </button>
            </div>
          )
        })}
      </div>
      <button
        onClick={() => navigate('/upload')}
        disabled={!allGranted}
        className="mt-8 w-full py-2.5 rounded-md bg-stamp text-paper text-sm font-medium disabled:opacity-40"
      >
        Continue to import
      </button>
    </div>
  )
}
