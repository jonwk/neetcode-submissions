class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        minPrice = 0
        minIndex = 0
        
        for price, index in enumerate(prices):
            if price < minPrice:
                minPrice = price
                minIndex = index
        
        print(minPrice)
        for i in range(minIndex, len(prices)):
            profit = minPrice - prices[i]
            maxProfit = max(maxProfit, profit)

        return maxProfit

            

        