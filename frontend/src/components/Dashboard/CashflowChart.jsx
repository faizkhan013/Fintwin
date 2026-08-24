import React from 'react'
import {
  ResponsiveContainer, ComposedChart, Area, Line, XAxis, YAxis,
  CartesianGrid, Tooltip, ReferenceLine, Legend,
} from 'recharts'

function currency(v) {
  if (v == null) return '—'
  return `₹${Math.round(v).toLocaleString('en-IN')}`
}

function CustomTooltip({ active, payload, label }) {
  if (!active || !payload?.length) return null
  return (
    <div className="ledger-card px-3 py-2 text-xs font-mono">
      <p className="text-muted mb-1">{label}</p>
      {payload.map((p) => (
        <p key={p.dataKey} style={{ color: p.color }}>
          {p.name}: {currency(p.value)}
        </p>
      ))}
    </div>
  )
}

export default function CashflowChart({ data, shockedData }) {
  const merged = data.map((d, i) => ({
    ...d,
    shocked: shockedData ? shockedData[i]?.shocked : undefined,
  }))

  return (
    <div className="ledger-card p-4 md:p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="font-display text-lg">Balance forecast</h3>
        <div className="flex gap-4 text-xs font-mono text-muted">
          <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded-full bg-verified inline-block" /> Actual</span>
          <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded-full bg-brass inline-block" /> Projected</span>
          {shockedData && <span className="flex items-center gap-1"><span className="w-2.5 h-2.5 rounded-full bg-stamp inline-block" /> Under shock</span>}
        </div>
      </div>
      <ResponsiveContainer width="100%" height={280}>
        <ComposedChart data={merged} margin={{ top: 4, right: 8, left: 0, bottom: 0 }}>
          <CartesianGrid stroke="rgba(42,42,38,0.08)" vertical={false} />
          <XAxis dataKey="date" tick={{ fontSize: 11, fontFamily: 'IBM Plex Mono' }} axisLine={{ stroke: 'rgba(42,42,38,0.15)' }} tickLine={false} />
          <YAxis tick={{ fontSize: 11, fontFamily: 'IBM Plex Mono' }} axisLine={false} tickLine={false} tickFormatter={(v) => `₹${(v / 1000).toFixed(0)}k`} />
          <Tooltip content={<CustomTooltip />} />
          <ReferenceLine y={0} stroke="#B23A2E" strokeDasharray="4 3" label={{ value: 'Liquidity floor', position: 'insideTopRight', fontSize: 10, fill: '#B23A2E' }} />
          <Area type="monotone" dataKey="balance" stroke="#3F6B4F" fill="#3F6B4F" fillOpacity={0.12} strokeWidth={2} name="Actual" connectNulls={false} />
          <Line type="monotone" dataKey="projected" stroke="#B08D57" strokeWidth={2} strokeDasharray="5 3" dot={{ r: 3 }} name="Projected" />
          {shockedData && (
            <Line type="monotone" dataKey="shocked" stroke="#B23A2E" strokeWidth={2} dot={{ r: 3 }} name="Under shock" />
          )}
        </ComposedChart>
      </ResponsiveContainer>
    </div>
  )
}
