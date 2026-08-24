import React, { useEffect, useState } from 'react'
import SectionHeader from '../components/common/SectionHeader'
import Loader from '../components/common/Loader'
import ShockControls from '../components/SimulationPanel/ShockControls'
import SimulationResultChart from '../components/SimulationPanel/SimulationResultChart'
import { getBalanceSeries } from '../api/twinApi'
import { getShockPresets, runSimulation } from '../api/analyticsApi'

export default function SimulationPage() {
  const [series, setSeries] = useState(null)
  const [presets, setPresets] = useState(null)
  const [selected, setSelected] = useState(null)
  const [shocked, setShocked] = useState(null)
  const [running, setRunning] = useState(false)

  useEffect(() => {
    getBalanceSeries().then(setSeries)
    getShockPresets().then(setPresets)
  }, [])

  const handleRun = async () => {
    setRunning(true)
    const res = await runSimulation(selected)
    setShocked(res)
    setRunning(false)
  }

  return (
    <div className="max-w-6xl mx-auto px-6 py-10">
      <SectionHeader
        eyebrow="Simulate"
        title="Stress-test your cash flow"
        subtitle="See how a shock — a late payment, a lost customer, a cost spike — would move your projected balance, before it happens."
      />
      {!series || !presets ? <Loader label="Preparing scenarios…" /> : (
        <div className="grid md:grid-cols-3 gap-6">
          <div className="md:col-span-1">
            <ShockControls presets={presets} selected={selected} onSelect={setSelected} onRun={handleRun} running={running} />
          </div>
          <div className="md:col-span-2">
            <SimulationResultChart balanceSeries={series} shockedSeries={shocked} />
          </div>
        </div>
      )}
    </div>
  )
}
