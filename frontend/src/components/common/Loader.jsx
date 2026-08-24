import React from 'react'

export default function Loader({ label = 'Loading…' }) {
  return (
    <div className="flex items-center gap-2 text-muted text-sm py-6">
      <span className="w-3 h-3 rounded-full border-2 border-brass border-t-transparent animate-spin" />
      {label}
    </div>
  )
}
