import React from 'react'
import ExplainStamp from '../common/ExplainStamp'

const severityStyle = {
  high: 'border-l-stamp',
  medium: 'border-l-brass',
  low: 'border-l-verified',
}

export default function RiskFlagCard({ flag }) {
  return (
    <div className={`ledger-card perforated-top border-l-4 ${severityStyle[flag.severity]} p-4 flex items-start justify-between gap-3`}>
      <div>
        <p className="font-mono text-[10px] uppercase tracking-wide text-muted mb-1">{flag.type}</p>
        <p className="text-sm text-charcoal leading-snug">{flag.message}</p>
      </div>
      <ExplainStamp severity={flag.severity} reasoning={flag.reasoning} numbers={flag.numbers} />
    </div>
  )
}
