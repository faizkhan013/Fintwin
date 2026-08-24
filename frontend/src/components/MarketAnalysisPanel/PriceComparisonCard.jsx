import React from 'react'

export default function PriceComparisonCard({ data }) {
  if (!data) return null
  const ratingColor = data.rating === 'Fairly priced' ? 'text-verified' : 'text-brass'
  return (
    <div className="ledger-card p-4 md:p-6">
      <h3 className="font-display text-lg mb-1">{data.product}</h3>
      <p className={`text-sm font-medium mb-4 ${ratingColor}`}>{data.rating}</p>
      <div className="grid grid-cols-4 gap-3 text-center">
        <div>
          <p className="text-[11px] font-mono uppercase text-muted">Your price</p>
          <p className="font-display text-lg tabular">₹{data.yourPrice}</p>
        </div>
        <div>
          <p className="text-[11px] font-mono uppercase text-muted">Market low</p>
          <p className="font-display text-lg tabular">₹{data.marketLow}</p>
        </div>
        <div>
          <p className="text-[11px] font-mono uppercase text-muted">Market avg</p>
          <p className="font-display text-lg tabular">₹{data.marketAvg}</p>
        </div>
        <div>
          <p className="text-[11px] font-mono uppercase text-muted">Market high</p>
          <p className="font-display text-lg tabular">₹{data.marketHigh}</p>
        </div>
      </div>
      <p className="text-xs text-muted mt-4">
        Only applies to non-MRP-fixed products. Comparison is informational, not a pricing directive.
      </p>
    </div>
  )
}
