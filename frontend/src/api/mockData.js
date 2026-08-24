// Sample data standing in for the Django/DRF + analytics-engine responses.
// Every field here maps 1:1 to what the real endpoints are expected to return,
// so swapping mockApi -> real axios calls later shouldn't require UI changes.

export const mockBalanceSeries = [
  { date: 'Wk 1', balance: 182000, projected: 182000 },
  { date: 'Wk 2', balance: 164000, projected: 164000 },
  { date: 'Wk 3', balance: 141000, projected: 141000 },
  { date: 'Wk 4', balance: 98000, projected: 98000 },
  { date: 'Wk 5', balance: null, projected: 52000 },
  { date: 'Wk 6', balance: null, projected: -18000 },
  { date: 'Wk 7', balance: null, projected: 6000 },
  { date: 'Wk 8', balance: null, projected: 41000 },
]

export const mockSummary = {
  currentBalance: 182000,
  liquidityGapDate: 'Wk 6',
  liquidityGapAmount: -18000,
  avgMonthlyInflow: 340000,
  avgMonthlyOutflow: 312000,
}

export const mockInvoices = [
  { id: 'INV-1042', customer: 'Anand Textiles', amount: 84000, dueDate: '2026-08-22', status: 'overdue', daysOverdue: 14, amountPaid: 30000, rolloverCount: 1 },
  { id: 'INV-1050', customer: 'Rao Hardware Co.', amount: 46500, dueDate: '2026-08-28', status: 'due_soon', daysOverdue: 0, amountPaid: 0, rolloverCount: 0 },
  { id: 'INV-1055', customer: 'Anand Textiles', amount: 61000, dueDate: '2026-09-02', status: 'upcoming', daysOverdue: 0, amountPaid: 0, rolloverCount: 0 },
  { id: 'INV-1061', customer: 'Sundar Retail Group', amount: 132000, dueDate: '2026-08-10', status: 'overdue', daysOverdue: 26, amountPaid: 0, rolloverCount: 2 },
  { id: 'INV-1066', customer: 'Priya Enterprises', amount: 27500, dueDate: '2026-09-05', status: 'upcoming', daysOverdue: 0, amountPaid: 0, rolloverCount: 0 },
]

export const mockPendingImports = [
  { id: 'PI-201', source: 'invoice_scan_08.jpg', extracted: { customer: 'Anand Textiles', amount: '84,000', dueDate: '2026-08-22', invoiceNo: 'INV-1042' }, confidence: 0.91 },
  { id: 'PI-202', source: 'gst_einvoice.json', extracted: { customer: 'Rao Hardware Co.', amount: '46,500', dueDate: '2026-08-28', invoiceNo: 'INV-1050' }, confidence: 0.99 },
]

export const mockRiskFlags = [
  {
    id: 'risk-1',
    type: 'Concentration risk',
    severity: 'high',
    message: 'Anand Textiles accounts for 41% of your outstanding receivables.',
    reasoning: 'Your concentration threshold is 30% of total receivables. Anand Textiles currently holds ₹1,45,000 of ₹3,51,000 outstanding (41.3%). Losing or delaying this one customer would materially affect your cash position.',
    numbers: { customerShare: '41.3%', threshold: '30%', outstandingFromCustomer: '₹1,45,000' },
  },
  {
    id: 'risk-2',
    type: 'Delayed-payment risk',
    severity: 'medium',
    message: 'Sundar Retail Group is paying 26 days later than their usual pattern.',
    reasoning: 'Average historical delay for this customer was 6 days. The current invoice (INV-1061) is 26 days overdue, a 20-day increase versus baseline, which is flagged once delay grows beyond 14 days.',
    numbers: { historicalAvgDelay: '6 days', currentDelay: '26 days', deltaThreshold: '14 days' },
  },
  {
    id: 'risk-3',
    type: 'Liquidity gap',
    severity: 'high',
    message: 'Projected balance turns negative in Week 6 (≈ −₹18,000).',
    reasoning: 'Forecast combines confirmed receivables, recurring expenses and payment-history trends. Without intervention, outflows exceed inflows starting Week 6, based on a 4-week moving average of your last 6 months of cash movement.',
    numbers: { projectedGap: '−₹18,000', gapWeek: 'Week 6' },
  },
]

export const mockBankRates = [
  { bank: 'Suvidha Co-operative Bank', product: 'Working Capital Loan', interestRate: 11.5, processingFeePct: 0.5, tenureMonths: 6 },
  { bank: 'Nirman MSME Bank', product: 'Working Capital Loan', interestRate: 12.75, processingFeePct: 1.0, tenureMonths: 6 },
  { bank: 'Vyapaar Finance NBFC', product: 'Invoice Discounting', interestRate: 14.0, processingFeePct: 0.75, tenureMonths: 3 },
  { bank: 'Setu Digital Lender', product: 'Invoice Discounting', interestRate: 15.5, processingFeePct: 0.25, tenureMonths: 3 },
]

export const mockFinancingOptions = [
  { option: 'Non-debt (owner buffer / grant)', totalCost: 0, speed: 'Immediate, if available', notes: 'No dilution of receivables, but depends on your own reserve or grant eligibility — not always available.' },
  { option: 'Invoice financing (Vyapaar Finance NBFC)', totalCost: 3675, speed: '1–2 days', notes: 'Fee-based, tied to the specific invoice; does not add a repayment obligation beyond the invoice value.' },
  { option: 'Working capital loan (Suvidha Co-operative Bank)', totalCost: 6210, speed: '3–5 days', notes: 'Lowest interest among compared banks; requires collateral/credit check.' },
]

export const mockOpportunityCost = {
  loanOptionCost: 6210,
  waitingCostEstimate: 9400,
  waitingCostBasis: 'Estimated cost of a stalled reorder and a 2% early-payment discount you would otherwise offer to accelerate collection.',
  verdict: 'loan_cheaper',
}

export const mockSavingsAdvice = {
  recommendedPct: 15,
  inflowVolatility: '22%',
  reasoning: 'Your monthly inflow has varied by 22% over the last 6 months. Businesses with variance above 20% are advised to hold a 15% buffer of average monthly income as an emergency reserve.',
}

export const mockSurvivability = {
  survivableLossAmount: 156000,
  survivableWeeks: 5,
  reasoning: 'Based on your average monthly expenses of ₹1,04,000 and current reserve, your business can absorb roughly 5 weeks of lost income before liquidity turns negative.',
}

export const mockRecoverySteps = [
  { step: 1, action: 'Follow up on Sundar Retail Group (26 days overdue, ₹1,32,000)', impact: 'Recovers the single largest overdue amount and directly closes the Week 6 gap.' },
  { step: 2, action: 'Offer Anand Textiles a partial-payment plan on INV-1042', impact: 'Reduces concentration risk while keeping the relationship, instead of a single lump demand.' },
  { step: 3, action: 'Delay non-essential recurring expense scheduled for Wk 5', impact: 'Buys one additional week of runway without external financing.' },
  { step: 4, action: 'If gap remains, use invoice financing on INV-1050 (lowest cost option compared)', impact: 'Closes remaining gap at an estimated ₹3,675 total cost.' },
]

export const mockShockPresets = [
  { id: 'late_payment', label: 'Biggest customer pays 30 days late' },
  { id: 'lost_customer', label: 'Lose top 2 customers' },
  { id: 'expense_spike', label: 'Expenses rise 15% next month' },
]

export const mockMarketComparison = {
  product: 'Cotton Bedsheet Set (Queen)',
  yourPrice: 1450,
  marketLow: 1190,
  marketHigh: 1780,
  marketAvg: 1465,
  rating: 'Fairly priced',
}
