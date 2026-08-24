import React from 'react'

export default function FieldEditor({ label, value, onChange }) {
  return (
    <label className="block">
      <span className="text-[11px] font-mono uppercase tracking-wide text-muted capitalize">
        {label.replace(/([A-Z])/g, ' $1')}
      </span>
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="mt-1 w-full rounded-md border border-charcoal/15 bg-paper px-2 py-1.5 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-brass/50"
      />
    </label>
  )
}
