import React, { useState } from 'react'

const severityColor = {
  high: 'text-stamp',
  medium: 'text-brass',
  low: 'text-verified',
  info: 'text-charcoal',
}

/**
 * Every risk flag / recommendation carries one of these.
 * It is the page's signature element: a small rotated "seal" that,
 * on click, unfolds the plain-English reasoning and the numbers behind it.
 * This exists specifically to satisfy "explain every recommendation" —
 * nothing on this platform should show a verdict without this attached.
 */
export default function ExplainStamp({ severity = 'info', reasoning, numbers }) {
  const [open, setOpen] = useState(false)

  return (
    <div className="relative">
      <button
        type="button"
        aria-expanded={open}
        aria-label="Why am I seeing this?"
        onClick={() => setOpen((o) => !o)}
        className={`explain-stamp ${severityColor[severity] || severityColor.info}`}
      >
        WHY
      </button>
      {open && (
        <div className="absolute right-0 z-20 mt-2 w-72 ledger-card p-4 text-left shadow-lg">
          <p className="font-mono text-[11px] uppercase tracking-wide text-muted mb-2">Reasoning</p>
          <p className="text-sm leading-relaxed text-charcoal mb-3">{reasoning}</p>
          {numbers && (
            <dl className="grid grid-cols-2 gap-x-2 gap-y-1 border-t border-charcoal/10 pt-2">
              {Object.entries(numbers).map(([k, v]) => (
                <React.Fragment key={k}>
                  <dt className="text-[11px] text-muted capitalize">{k.replace(/([A-Z])/g, ' $1')}</dt>
                  <dd className="text-[11px] font-mono text-right tabular">{v}</dd>
                </React.Fragment>
              ))}
            </dl>
          )}
        </div>
      )}
    </div>
  )
}
