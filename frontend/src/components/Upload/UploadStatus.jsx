import React from 'react'

const statusLabel = {
  processing: 'Reading with OCR…',
  ready_for_review: 'Ready for your review',
  confirmed: 'Confirmed',
}

export default function UploadStatus({ items }) {
  if (!items.length) return null
  return (
    <div className="ledger-card p-4 mt-4">
      <p className="font-mono text-[11px] uppercase tracking-wide text-muted mb-2">Upload queue</p>
      <ul className="space-y-2">
        {items.map((it) => (
          <li key={it.id} className="flex items-center justify-between text-sm">
            <span className="truncate">{it.fileName}</span>
            <span className="text-xs font-mono text-brass">{statusLabel[it.status] || it.status}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}
