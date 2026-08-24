import axiosClient from './axiosClient'

export async function compareProductPrice(productName = '', currentPrice = 0) {
  const response = await axiosClient.get('/market/compare/', {
    params: { product: productName, price: currentPrice },
  })
  return response.data
}
