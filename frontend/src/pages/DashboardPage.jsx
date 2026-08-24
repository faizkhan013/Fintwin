import React, { useEffect, useState } from 'react'
import SectionHeader from '../components/common/SectionHeader'
import Loader from '../components/common/Loader'
import SummaryCards from '../components/Dashboard/SummaryCards'
import CashflowChart from '../components/Dashboard/CashflowChart'
import BalanceTimeline from '../components/Dashboard/BalanceTimeline'
import RiskFlagCard from '../components/RiskPanel/RiskFlagCard'
import SurvivablePercentCard from '../components/RiskPanel/SurvivablePercentCard'
import EmergencySavingsCard from '../components/RiskPanel/EmergencySavingsCard'
import { getSummary, getBalanceSeries, getInvoices } from '../api/twinApi'
import { getRiskFlags, getSavingsAdvice, getSurvivability } from '../api/analyticsApi'
import { useAuth } from '../context/AuthContext'

export default function DashboardPage() {
  const { user } = useAuth()
  const [summary, setSummary] = useState(null)
  const [series, setSeries] = useState(null)
  const [invoices, setInvoices] = useState(null)
  const [riskFlags, setRiskFlags] = useState(null)
  const [savings, setSavings] = useState(null)
  const [survivability, setSurvivability] = useState(null)

  useEffect(() => {
    getSummary().then(setSummary)
    getBalanceSeries().then(setSeries)
    getInvoices().then(setInvoices)
    getRiskFlags().then(setRiskFlags)
    getSavingsAdvice().then(setSavings)
    getSurvivability().then(setSurvivability)
  }, [])

  const loading = !summary || !series || !invoices || !riskFlags

  return (
    <div className="max-w-6xl mx-auto px-6 py-10">
      <SectionHeader
        eyebrow="Ledger"
        title={`Welcome back, ${user?.businessName || 'there'}`}
        subtitle="Your cash-flow digital twin, built from consented invoices, expenses and payment history."
      />
      {loading ? <Loader label="Building your twin…" /> : (
        <div className="space-y-8">
          <SummaryCards summary={summary} />
          <CashflowChart data={series} />
          <div className="grid md:grid-cols-2 gap-4">
            <SurvivablePercentCard data={survivability} />
            <EmergencySavingsCard data={savings} />
          </div>
          <div>
            <h2 className="font-display text-xl mb-3">Risk flags</h2>
            <div className="space-y-3">
              {riskFlags.map((f) => <RiskFlagCard key={f.id} flag={f} />)}
            </div>
          </div>
          <BalanceTimeline invoices={invoices} />
        </div>
      )}
    </div>
  )
}
