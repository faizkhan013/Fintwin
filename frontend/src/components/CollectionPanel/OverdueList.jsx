import React from 'react'
import RolloverBadge from './RolloverBadge'

export default function OverdueList({ invoices, onFlagFollowUp, onOpenPartialPayment }) {
  const overdue = invoices.filter((i) => i.status === 'overdue')
  if (!overdue.length) {
    return <div className="ledger-card p-6 text-sm text-muted">No overdue invoices right now.</div>
  }
  return (
    <div className="ledger-card p-4 md:p-6">
      <h3 className="font-display text-lg mb-4">Overdue receivables</h3>
      <ul className="space-y-3">
        {overdue.map((inv) => (
          <li key={inv.id} className="flex flex-wrap items-center justify-between gap-3 border-b border-charcoal/5 pb-3 last:border-0">
            <div>
              <p className="text-sm font-medium">{inv.customer} — {inv.id}</p>
              <p className="text-xs text-muted">
                ₹{(inv.amount - inv.amountPaid).toLocaleString('en-IN')} outstanding · {inv.daysOverdue} days overdue
                {inv.amountPaid > 0 && <span> · ₹{inv.amountPaid.toLocaleString('en-IN')} already paid</span>}
              </p>
            </div>
            <div className="flex items-center gap-2">
              <RolloverBadge count={inv.rolloverCount} />
              <button
                onClick={() => onOpenPartialPayment(inv)}
                className="text-xs font-medium px-3 py-1.5 rounded-md border border-charcoal/15 hover:bg-charcoal/5"
              >
                Log partial payment
              </button>
              <button
                onClick={() => onFlagFollowUp(inv)}
                className="text-xs font-medium px-3 py-1.5 rounded-md bg-ink text-paper hover:bg-inkdeep"
              >
                Flag for follow-up
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}
