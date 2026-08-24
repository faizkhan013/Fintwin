import React from 'react'
import ExplainStamp from '../common/ExplainStamp'

export default function SurvivablePercentCard({ data }) {
  if (!data) return null
  return (
    <div className="ledger-card p-4 flex items-start justify-between gap-3">
      <div>
        <p className="font-mono text-[10px] uppercase tracking-wide text-muted mb-1">Loss-survivable buffer</p>
        <p className="font-display text-xl text-ink">₹{data.survivableLossAmount.toLocaleString('en-IN')} <span className="text-sm text-muted font-body">(~{data.survivableWeeks} weeks)</span></p>
      </div>
      <ExplainStamp severity="info" reasoning={data.reasoning} />
    </div>
  )
}
