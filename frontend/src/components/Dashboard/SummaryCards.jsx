import React from 'react'

function Card({ label, value, accent, sub }) {
  return (
    <div className="ledger-card p-4">
      <p className="font-mono text-[11px] uppercase tracking-wide text-muted mb-2">{label}</p>
      <p className={`font-display text-2xl tabular ${accent || 'text-ink'}`}>{value}</p>
      {sub && <p className="text-xs text-muted mt-1">{sub}</p>}
    </div>
  )
}

export default function SummaryCards({ summary }) {
  if (!summary) return null
  const gapNegative = summary.liquidityGapAmount < 0
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      <Card label="Current balance" value={`₹${summary.currentBalance.toLocaleString('en-IN')}`} />
      <Card
        label="Liquidity gap"
        value={`₹${summary.liquidityGapAmount.toLocaleString('en-IN')}`}
        accent={gapNegative ? 'text-stamp' : 'text-verified'}
        sub={`Projected in ${summary.liquidityGapDate}`}
      />
      <Card label="Avg. monthly inflow" value={`₹${summary.avgMonthlyInflow.toLocaleString('en-IN')}`} />
      <Card label="Avg. monthly outflow" value={`₹${summary.avgMonthlyOutflow.toLocaleString('en-IN')}`} />
    </div>
  )
}
