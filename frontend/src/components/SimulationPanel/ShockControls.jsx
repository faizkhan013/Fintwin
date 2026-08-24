import React from 'react'

export default function ShockControls({ presets, selected, onSelect, onRun, running }) {
  return (
    <div className="ledger-card p-4 md:p-6">
      <h3 className="font-display text-lg mb-3">Test a shock</h3>
      <div className="space-y-2 mb-4">
        {presets.map((p) => (
          <label key={p.id} className="flex items-center gap-2 text-sm cursor-pointer">
            <input
              type="radio"
              name="shock"
              checked={selected === p.id}
              onChange={() => onSelect(p.id)}
              className="accent-stamp"
            />
            {p.label}
          </label>
        ))}
      </div>
      <button
        onClick={onRun}
        disabled={!selected || running}
        className="text-sm font-medium px-4 py-2 rounded-md bg-stamp text-paper disabled:opacity-40 hover:opacity-90"
      >
        {running ? 'Running…' : 'Run simulation'}
      </button>
    </div>
  )
}
