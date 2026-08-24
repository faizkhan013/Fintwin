import React from 'react'

export default function LoanRateTable({ rates }) {
  const sorted = [...rates].sort((a, b) => a.interestRate - b.interestRate)
  return (
    <div className="ledger-card p-4 md:p-6 overflow-x-auto">
      <h3 className="font-display text-lg mb-4">Bank & lender rates</h3>
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-[11px] font-mono uppercase tracking-wide text-muted border-b border-charcoal/10">
            <th className="pb-2 pr-4">Lender</th>
            <th className="pb-2 pr-4">Product</th>
            <th className="pb-2 pr-4">Interest</th>
            <th className="pb-2 pr-4">Processing fee</th>
            <th className="pb-2">Tenure</th>
          </tr>
        </thead>
        <tbody>
          {sorted.map((r, i) => (
            <tr key={r.bank} className={`border-b border-charcoal/5 last:border-0 ${i === 0 ? 'bg-verified/5' : ''}`}>
              <td className="py-3 pr-4 font-medium">{r.bank} {i === 0 && <span className="text-[10px] font-mono text-verified ml-1">LOWEST</span>}</td>
              <td className="py-3 pr-4 text-muted">{r.product}</td>
              <td className="py-3 pr-4 font-mono tabular">{r.interestRate}%</td>
              <td className="py-3 pr-4 font-mono tabular">{r.processingFeePct}%</td>
              <td className="py-3 font-mono tabular">{r.tenureMonths} mo</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
