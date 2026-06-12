class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        def dfs(index,buy):
            if index>=n:
                return 0
            profit=0
            if(buy):
                profit=max(profit,-prices[index]+dfs(index+1,0),dfs(index+1,1))
            else:
                profit=max(profit,prices[index]+dfs(index+2,1),dfs(index+1,0))
            return profit
        return dfs(0,1)
                
        