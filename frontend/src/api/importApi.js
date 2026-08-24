import axiosClient, { unwrapList } from './axiosClient'

function normalizeImport(item) {
  const invoice = item.invoices?.[0]
  return {
    ...item,
    id: item.id,
    fileName: item.file_name || item.file?.split('/').pop() || 'import',
    source: item.file_name || item.file || 'uploaded file',
    status: item.status === 'review' ? 'ready_for_review' : item.status,
    extracted: invoice ? {
      customer: invoice.customer_name,
      amount: String(invoice.amount),
      dueDate: invoice.due_date,
      invoiceNo: invoice.invoice_number,
      invoiceId: invoice.id,
    } : {},
    confidence: invoice?.confidence_score || 0,
  }
}

export async function uploadFile(file) {
  const form = new FormData()
  form.append('file', file)
  const response = await axiosClient.post('/imports/upload/', form)
  return normalizeImport(response.data)
}

export async function getPendingImports() {
  const response = await axiosClient.get('/imports/pending/')
  return unwrapList(response.data).map(normalizeImport)
}

export async function confirmImport(id, correctedFields) {
  const response = await axiosClient.post(`/imports/${id}/confirm/`, {
    invoice_number: correctedFields.invoiceNo,
    customer_name: correctedFields.customer,
    amount: Number(String(correctedFields.amount).replace(/,/g, '')),
    due_date: correctedFields.dueDate,
  })
  return normalizeImport(response.data)
}
