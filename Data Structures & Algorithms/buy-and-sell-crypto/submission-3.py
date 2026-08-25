class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        minPrice = prices[0]
        minIndex = 0
        
        for index, price in enumerate(prices):
            if price <= minPrice:
                minPrice = price
                minIndex = index
        
        print(minPrice, minIndex)
        for i in range(minIndex, len(prices)):
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)

        return maxProfit

            

        