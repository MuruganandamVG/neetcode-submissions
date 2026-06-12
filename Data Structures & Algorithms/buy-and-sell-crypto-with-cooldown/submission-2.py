class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        # dp=[[-1]*2 for _ in range(n)]
        # def dfs(index,buy):
        #     if index>=n:
        #         return 0
        #     if dp[index][buy]!=-1:
        #         return dp[index][buy]
        #     profit=0
        #     if(buy):
        #         profit=max(profit,-prices[index]+dfs(index+1,0),dfs(index+1,1))
        #     else:
        #         profit=max(profit,prices[index]+dfs(index+2,1),dfs(index+1,0))
        #     dp[index][buy]=profit
        #     return dp[index][buy]
        # return dfs(0,1)

        # Bottom up solution 
        dp=[[0]*2 for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                profit=0
                if (buy):
                    profit=max(profit,-prices[i]+dp[i+1][0],dp[i+1][1])
                else:
                    profit=max(profit,prices[i]+dp[i+2][1],dp[i+1][0])
                dp[i][buy]=profit
        return dp[0][1]

                
        