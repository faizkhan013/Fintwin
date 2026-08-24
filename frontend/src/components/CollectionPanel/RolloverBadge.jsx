import React from 'react'

export default function RolloverBadge({ count }) {
  if (!count) return null
  return (
    <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-stamp/10 text-stamp">
      Rolled over ×{count}
    </span>
  )
}
