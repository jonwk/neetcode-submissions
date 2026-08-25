class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        
        while left < right and right < len(prices):
            profit = price[right] - price[left]
            if profit < maxProfit:
                left += 1
                rigth += 1
            else:
                maxProfit = profit
                right += 1

        return maxProfit    

        