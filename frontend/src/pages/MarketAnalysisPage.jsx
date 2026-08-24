import React, { useEffect, useState } from 'react'
import SectionHeader from '../components/common/SectionHeader'
import Loader from '../components/common/Loader'
import PriceComparisonCard from '../components/MarketAnalysisPanel/PriceComparisonCard'
import { compareProductPrice } from '../api/marketApi'

export default function MarketAnalysisPage() {
  const [query, setQuery] = useState('')
  const [result, setResult] = useState(undefined)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    compareProductPrice().then((r) => setResult(r))
  }, [])

  const handleSearch = async (e) => {
    e.preventDefault()
    setLoading(true)
    const r = await compareProductPrice(query)
    setResult(r)
    setLoading(false)
  }

  return (
    <div className="max-w-2xl mx-auto px-6 py-10">
      <SectionHeader
        eyebrow="Market · optional"
        title="How does your price compare?"
        subtitle="For products without a fixed MRP. This is a separate, lightweight tool — not part of your cash-flow risk score."
      />
      <form onSubmit={handleSearch} className="flex gap-2 mb-6">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g. Cotton bedsheet set (queen)"
          className="flex-1 rounded-md border border-charcoal/15 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-brass/50"
        />
        <button type="submit" className="px-4 py-2 rounded-md bg-ink text-paper text-sm font-medium hover:bg-inkdeep">
          Compare
        </button>
      </form>
      {loading || result === undefined ? <Loader label="Comparing market prices…" /> : <PriceComparisonCard data={result} />}
    </div>
  )
}
