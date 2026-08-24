import React from 'react'

export default function ComparisonTable({ options }) {
  return (
    <div className="ledger-card p-4 md:p-6 overflow-x-auto">
      <h3 className="font-display text-lg mb-4">Options compared</h3>
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-[11px] font-mono uppercase tracking-wide text-muted border-b border-charcoal/10">
            <th className="pb-2 pr-4">Option</th>
            <th className="pb-2 pr-4">Total cost</th>
            <th className="pb-2 pr-4">Speed</th>
            <th className="pb-2">Notes</th>
          </tr>
        </thead>
        <tbody>
          {options.map((o) => (
            <tr key={o.option} className="border-b border-charcoal/5 last:border-0">
              <td className="py-3 pr-4 font-medium">{o.option}</td>
              <td className="py-3 pr-4 font-mono tabular">{o.totalCost === 0 ? '₹0' : `₹${o.totalCost.toLocaleString('en-IN')}`}</td>
              <td className="py-3 pr-4 text-muted">{o.speed}</td>
              <td className="py-3 text-muted max-w-xs">{o.notes}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p className="text-xs text-muted mt-3">
        This is a comparison only — no option is auto-selected. You choose what to act on.
      </p>
    </div>
  )
}
