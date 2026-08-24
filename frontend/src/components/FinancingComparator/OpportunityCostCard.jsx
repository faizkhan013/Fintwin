import React from 'react'
import ExplainStamp from '../common/ExplainStamp'

export default function OpportunityCostCard({ data }) {
  if (!data) return null
  const cheaper = data.verdict === 'loan_cheaper' ? 'Taking the loan' : 'Waiting for the invoice'
  return (
    <div className="ledger-card p-4 md:p-6">
      <div className="flex items-start justify-between gap-3 mb-4">
        <h3 className="font-display text-lg">Loan vs. waiting — which costs more?</h3>
        <ExplainStamp
          severity="info"
          reasoning={data.waitingCostBasis}
          numbers={{ loanCost: `₹${data.loanOptionCost.toLocaleString('en-IN')}`, waitingCost: `₹${data.waitingCostEstimate.toLocaleString('en-IN')}` }}
        />
      </div>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <p className="text-[11px] font-mono uppercase text-muted">Loan cost</p>
          <p className="font-display text-2xl tabular">₹{data.loanOptionCost.toLocaleString('en-IN')}</p>
        </div>
        <div>
          <p className="text-[11px] font-mono uppercase text-muted">Estimated waiting cost</p>
          <p className="font-display text-2xl tabular">₹{data.waitingCostEstimate.toLocaleString('en-IN')}</p>
        </div>
      </div>
      <p className="text-sm text-verified mt-4 font-medium">{cheaper} is estimated to cost less.</p>
    </div>
  )
}
