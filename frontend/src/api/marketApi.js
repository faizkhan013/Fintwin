import axiosClient, { mockDelay } from './axiosClient'
import { mockMarketComparison } from './mockData'

export async function compareProductPrice(productName) {
  // Real call: return (await axiosClient.get('/market-analysis/compare/', { params: { productName } })).data
  return mockDelay({ ...mockMarketComparison, product: productName || mockMarketComparison.product }, 600)
}
