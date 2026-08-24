import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import SectionHeader from '../components/common/SectionHeader'
import Loader from '../components/common/Loader'
import ImportReviewTable from '../components/CorrectionScreen/ImportReviewTable'
import { getPendingImports, confirmImport } from '../api/importApi'

export default function CorrectionPage() {
  const [items, setItems] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    getPendingImports().then(setItems)
  }, [])

  const handleConfirm = async (id, fields) => {
    await confirmImport(id, fields)
    setItems((prev) => prev.filter((it) => it.id !== id))
  }

  return (
    <div className="max-w-3xl mx-auto px-6 py-10">
      <SectionHeader
        eyebrow="Review"
        title="Check what we read"
        subtitle="OCR isn't perfect. Fix any field before it becomes part of your cash-flow twin — nothing is saved until you confirm it."
      />
      {items === null ? <Loader label="Loading pending imports…" /> : (
        <>
          <ImportReviewTable items={items} onConfirm={handleConfirm} />
          <button
            onClick={() => navigate('/dashboard')}
            className="mt-6 w-full py-2.5 rounded-md bg-verified text-paper text-sm font-medium hover:opacity-90"
          >
            Go to dashboard
          </button>
        </>
      )}
    </div>
  )
}
