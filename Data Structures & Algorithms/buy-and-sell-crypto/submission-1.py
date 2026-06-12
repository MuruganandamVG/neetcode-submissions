class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        n=len(prices)
        minPrice=float('inf')
        for i in range(n):
            minPrice=min(minPrice,prices[i])
            profit=max(profit,prices[i]-minPrice)
        return profit

        return profit