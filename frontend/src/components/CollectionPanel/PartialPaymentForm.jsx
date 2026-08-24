import React, { useState } from 'react'

export default function PartialPaymentForm({ invoice, onSubmit, onClose }) {
  const [amount, setAmount] = useState('')
  if (!invoice) return null

  return (
    <div className="fixed inset-0 bg-ink/40 flex items-center justify-center z-40 p-4">
      <div className="ledger-card p-6 w-full max-w-sm">
        <h3 className="font-display text-lg mb-1">Log partial payment</h3>
        <p className="text-sm text-muted mb-4">{invoice.customer} — {invoice.id}</p>
        <label className="block mb-4">
          <span className="text-[11px] font-mono uppercase text-muted">Amount received (₹)</span>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            className="mt-1 w-full rounded-md border border-charcoal/15 px-3 py-2 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-brass/50"
            placeholder="e.g. 20000"
            autoFocus
          />
        </label>
        <p className="text-xs text-muted mb-4">
          Any remaining balance stays open and rolls into next month if still unpaid at the due date.
        </p>
        <div className="flex gap-2 justify-end">
          <button onClick={onClose} className="text-sm px-4 py-2 rounded-md border border-charcoal/15">Cancel</button>
          <button
            onClick={() => { onSubmit(invoice.id, Number(amount)); onClose() }}
            disabled={!amount}
            className="text-sm px-4 py-2 rounded-md bg-verified text-paper disabled:opacity-40"
          >
            Save payment
          </button>
        </div>
      </div>
    </div>
  )
}
