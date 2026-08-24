import React, { useEffect, useState } from 'react'
import SectionHeader from '../components/common/SectionHeader'
import Loader from '../components/common/Loader'
import ComparisonTable from '../components/FinancingComparator/ComparisonTable'
import LoanRateTable from '../components/FinancingComparator/LoanRateTable'
import OpportunityCostCard from '../components/FinancingComparator/OpportunityCostCard'
import { getBankRates, getFinancingComparison, getOpportunityCost } from '../api/loanApi'

export default function FinancingPage() {
  const [rates, setRates] = useState(null)
  const [options, setOptions] = useState(null)
  const [oppCost, setOppCost] = useState(null)

  useEffect(() => {
    getBankRates().then(setRates)
    getFinancingComparison().then(setOptions)
    getOpportunityCost().then(setOppCost)
  }, [])

  const loading = !rates || !options || !oppCost

  return (
    <div className="max-w-4xl mx-auto px-6 py-10">
      <SectionHeader
        eyebrow="Financing"
        title="Compare your options"
        subtitle="Non-debt, invoice-finance and working-capital options, side by side, with full costs shown. Nothing here is an automatic lending decision — you choose."
      />
      {loading ? <Loader label="Comparing options…" /> : (
        <div className="space-y-6">
          <ComparisonTable options={options} />
          <LoanRateTable rates={rates} />
          <OpportunityCostCard data={oppCost} />
        </div>
      )}
    </div>
  )
}
