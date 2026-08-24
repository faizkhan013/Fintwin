import React from 'react'

export default function RecoveryStepsList({ steps }) {
  if (!steps?.length) return null
  return (
    <div className="ledger-card p-4 md:p-6">
      <h3 className="font-display text-lg mb-4">Suggested recovery steps</h3>
      <ol className="space-y-4">
        {steps.map((s) => (
          <li key={s.step} className="flex gap-4">
            <span className="font-display text-lg text-brass w-6 shrink-0">{s.step}</span>
            <div>
              <p className="text-sm font-medium">{s.action}</p>
              <p className="text-xs text-muted mt-0.5">{s.impact}</p>
            </div>
          </li>
        ))}
      </ol>
      <p className="text-xs text-muted mt-4 border-t border-charcoal/10 pt-3">
        These are suggestions in priority order, not automated actions. You decide what to act on.
      </p>
    </div>
  )
}
