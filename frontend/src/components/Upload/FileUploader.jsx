import React, { useCallback, useState } from 'react'

export default function FileUploader({ onUpload }) {
  const [dragOver, setDragOver] = useState(false)

  const handleFiles = useCallback((files) => {
    Array.from(files).forEach((file) => onUpload(file))
  }, [onUpload])

  return (
    <div
      onDragOver={(e) => { e.preventDefault(); setDragOver(true) }}
      onDragLeave={() => setDragOver(false)}
      onDrop={(e) => { e.preventDefault(); setDragOver(false); handleFiles(e.dataTransfer.files) }}
      className={`ledger-card border-2 border-dashed p-10 text-center transition-colors ${
        dragOver ? 'border-brass bg-brass/5' : 'border-charcoal/20'
      }`}
    >
      <p className="font-display text-lg text-ink mb-1">Drop invoices here</p>
      <p className="text-sm text-muted mb-4">Scanned PDFs, photos, CSV exports or GST e-invoice JSON</p>
      <label className="inline-block px-4 py-2 rounded-md bg-ink text-paper text-sm font-medium cursor-pointer hover:bg-inkdeep">
        Choose files
        <input
          type="file"
          multiple
          className="hidden"
          accept=".pdf,.jpg,.jpeg,.png,.csv,.json"
          onChange={(e) => handleFiles(e.target.files)}
        />
      </label>
    </div>
  )
}
