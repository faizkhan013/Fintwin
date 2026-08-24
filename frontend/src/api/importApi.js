import axiosClient, { mockDelay } from './axiosClient'
import { mockPendingImports } from './mockData'

export async function uploadFile(file) {
  // Real call:
  // const form = new FormData(); form.append('file', file)
  // return (await axiosClient.post('/imports/upload/', form, { headers: { 'Content-Type': 'multipart/form-data' } })).data
  return mockDelay({ id: `PI-${Math.floor(Math.random() * 900 + 100)}`, status: 'processing', fileName: file.name }, 900)
}

export async function getPendingImports() {
  // Real call: return (await axiosClient.get('/imports/pending/')).data
  return mockDelay(mockPendingImports)
}

export async function confirmImport(id, correctedFields) {
  // Real call: return (await axiosClient.post(`/imports/${id}/confirm/`, correctedFields)).data
  return mockDelay({ ok: true, id, correctedFields })
}
