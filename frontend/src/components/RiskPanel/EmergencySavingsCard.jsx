import React from 'react'
import ExplainStamp from '../common/ExplainStamp'

export default function EmergencySavingsCard({ data }) {
  if (!data) return null
  return (
    <div className="ledger-card p-4 flex items-start justify-between gap-3">
      <div>
        <p className="font-mono text-[10px] uppercase tracking-wide text-muted mb-1">Suggested emergency savings</p>
        <p className="font-display text-xl text-ink">{data.recommendedPct}% <span className="text-sm text-muted font-body">of monthly income</span></p>
      </div>
      <ExplainStamp severity="info" reasoning={data.reasoning} numbers={{ inflowVolatility: data.inflowVolatility }} />
    </div>
  )
}
