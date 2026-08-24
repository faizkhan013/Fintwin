import React from 'react'
import CashflowChart from '../Dashboard/CashflowChart'

export default function SimulationResultChart({ balanceSeries, shockedSeries }) {
  return <CashflowChart data={balanceSeries} shockedData={shockedSeries} />
}
