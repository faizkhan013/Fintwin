import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import SectionHeader from '../components/common/SectionHeader'
import FileUploader from '../components/Upload/FileUploader'
import UploadStatus from '../components/Upload/UploadStatus'
import { uploadFile } from '../api/importApi'

export default function UploadPage() {
  const [items, setItems] = useState([])
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const handleUpload = async (file) => {
    const tempId = `temp-${Date.now()}-${file.name}`
    setError('')
    setItems((prev) => [...prev, { id: tempId, fileName: file.name, status: 'processing' }])
    try {
      const res = await uploadFile(file)
      setItems((prev) => prev.map((it) => it.id === tempId ? { ...it, id: res.id, status: res.status || 'processing' } : it))
    } catch (err) {
      setItems((prev) => prev.map((it) => it.id === tempId ? { ...it, status: 'failed' } : it))
      setError(err.response?.data?.detail || 'Upload failed. Check the file type and try again.')
    }
  }

  const canReview = items.some((it) => ['review', 'ready_for_review'].includes(it.status))

  return (
    <div className="max-w-2xl mx-auto px-6 py-10">
      <SectionHeader eyebrow="Import" title="Bring in your invoices" subtitle="Upload scans, photos, CSV exports, or GST e-invoice JSON. Every extracted field is yours to check before it counts toward your twin." />
      <FileUploader onUpload={handleUpload} />
      {error && <p className="text-sm text-stamp mt-3">{error}</p>}
      <UploadStatus items={items} />
      {canReview && (
        <button onClick={() => navigate('/correction')} className="mt-6 w-full py-2.5 rounded-md bg-ink text-paper text-sm font-medium hover:bg-inkdeep">Review extracted data</button>
      )}
    </div>
  )
}
