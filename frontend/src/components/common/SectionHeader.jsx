import React from 'react'

export default function SectionHeader({ eyebrow, title, subtitle }) {
  return (
    <div className="mb-6">
      {eyebrow && (
        <p className="font-mono text-[11px] uppercase tracking-widest text-brass mb-1">{eyebrow}</p>
      )}
      <h1 className="font-display text-2xl md:text-3xl font-semibold text-ink">{title}</h1>
      {subtitle && <p className="text-muted text-sm mt-1 max-w-2xl">{subtitle}</p>}
    </div>
  )
}
