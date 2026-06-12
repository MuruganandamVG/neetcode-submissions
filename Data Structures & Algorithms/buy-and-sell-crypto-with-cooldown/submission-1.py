class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        def dfs(index,buy):
            if index>=n:
                return 0
            if dp[index][buy]!=-1:
                return dp[index][buy]
            profit=0
            if(buy):
                profit=max(profit,-prices[index]+dfs(index+1,0),dfs(index+1,1))
            else:
                profit=max(profit,prices[index]+dfs(index+2,1),dfs(index+1,0))
            dp[index][buy]=profit
            return dp[index][buy]
        return dfs(0,1)
                
        