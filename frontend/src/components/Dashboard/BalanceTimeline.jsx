import React from 'react'

export default function BalanceTimeline({ invoices }) {
  const sorted = [...invoices].sort((a, b) => new Date(a.dueDate) - new Date(b.dueDate))
  const statusColor = {
    overdue: 'bg-stamp',
    due_soon: 'bg-brass',
    upcoming: 'bg-verified',
  }
  const statusLabel = {
    overdue: 'Overdue',
    due_soon: 'Due soon',
    upcoming: 'Upcoming',
  }
  return (
    <div className="ledger-card p-4 md:p-6">
      <h3 className="font-display text-lg mb-4">Receivables timeline</h3>
      <ul className="space-y-3">
        {sorted.map((inv) => (
          <li key={inv.id} className="flex items-center gap-3 text-sm">
            <span className={`w-2 h-2 rounded-full ${statusColor[inv.status]}`} />
            <span className="font-mono text-xs text-muted w-24 shrink-0">{inv.dueDate}</span>
            <span className="flex-1 truncate">{inv.customer} — {inv.id}</span>
            <span className="font-mono tabular text-xs">₹{inv.amount.toLocaleString('en-IN')}</span>
            <span className="text-[11px] font-mono text-muted w-16 text-right">{statusLabel[inv.status]}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}
