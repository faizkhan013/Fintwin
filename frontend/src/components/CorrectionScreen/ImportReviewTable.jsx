import React, { useState } from 'react'
import FieldEditor from './FieldEditor'

export default function ImportReviewTable({ items, onConfirm }) {
  const [edited, setEdited] = useState(() =>
    Object.fromEntries(items.map((it) => [it.id, { ...it.extracted }]))
  )

  const updateField = (itemId, field, value) => {
    setEdited((prev) => ({ ...prev, [itemId]: { ...prev[itemId], [field]: value } }))
  }

  if (!items.length) {
    return (
      <div className="ledger-card p-8 text-center text-muted text-sm">
        Nothing waiting for review. Uploaded invoices will land here once OCR finishes.
      </div>
    )
  }

  return (
    <div className="space-y-4">
      {items.map((item) => (
        <div key={item.id} className="ledger-card perforated-top p-5">
          <div className="flex items-center justify-between mb-3">
            <p className="text-sm text-muted">{item.source}</p>
            <span className={`text-[11px] font-mono px-2 py-0.5 rounded-full ${
              item.confidence > 0.95 ? 'bg-verified/15 text-verified' : 'bg-brass/15 text-brass'
            }`}>
              {Math.round(item.confidence * 100)}% confidence
            </span>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
            {Object.entries(edited[item.id]).map(([field, value]) => (
              <FieldEditor
                key={field}
                label={field}
                value={value}
                onChange={(v) => updateField(item.id, field, v)}
              />
            ))}
          </div>
          <button
            onClick={() => onConfirm(item.id, edited[item.id])}
            className="text-sm font-medium px-4 py-2 rounded-md bg-verified text-paper hover:opacity-90"
          >
            Confirm & save
          </button>
        </div>
      ))}
    </div>
  )
}
