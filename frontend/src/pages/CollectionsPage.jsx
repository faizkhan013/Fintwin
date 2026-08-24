import React, { useEffect, useState } from 'react'
import SectionHeader from '../components/common/SectionHeader'
import Loader from '../components/common/Loader'
import OverdueList from '../components/CollectionPanel/OverdueList'
import PartialPaymentForm from '../components/CollectionPanel/PartialPaymentForm'
import RecoveryStepsList from '../components/RecoveryPlanPanel/RecoveryStepsList'
import { getInvoices } from '../api/twinApi'
import { getRecoveryPlan } from '../api/analyticsApi'
import { logPartialPayment, flagForFollowUp } from '../api/collectionApi'

export default function CollectionsPage() {
  const [invoices, setInvoices] = useState(null)
  const [recoverySteps, setRecoverySteps] = useState(null)
  const [activeInvoice, setActiveInvoice] = useState(null)
  const [toast, setToast] = useState(null)

  useEffect(() => {
    getInvoices().then(setInvoices)
    getRecoveryPlan().then(setRecoverySteps)
  }, [])

  const handleFlagFollowUp = async (invoice) => {
    await flagForFollowUp(invoice.invoiceId, 'Flagged from Collections page')
    setToast(`${invoice.customer} flagged for follow-up.`)
    setTimeout(() => setToast(null), 2500)
  }

  const handlePartialPayment = async (invoiceId, amount) => {
    await logPartialPayment(invoiceId, amount)
    setInvoices((prev) =>
      prev.map((inv) => (inv.id === invoiceId ? { ...inv, amountPaid: inv.amountPaid + amount } : inv))
    )
    setToast('Partial payment logged.')
    setTimeout(() => setToast(null), 2500)
  }

  return (
    <div className="max-w-4xl mx-auto px-6 py-10">
      <SectionHeader
        eyebrow="Collections"
        title="Close the gap"
        subtitle="Follow up on what's overdue, log partial payments, and work through a prioritized recovery plan. Unpaid balances roll forward automatically until settled."
      />
      {!invoices || !recoverySteps ? <Loader label="Loading receivables…" /> : (
        <div className="space-y-6">
          <OverdueList
            invoices={invoices}
            onFlagFollowUp={handleFlagFollowUp}
            onOpenPartialPayment={setActiveInvoice}
          />
          <RecoveryStepsList steps={recoverySteps} />
        </div>
      )}
      <PartialPaymentForm invoice={activeInvoice} onSubmit={handlePartialPayment} onClose={() => setActiveInvoice(null)} />
      {toast && (
        <div className="fixed bottom-6 right-6 ledger-card px-4 py-2 text-sm shadow-lg">{toast}</div>
      )}
    </div>
  )
}
