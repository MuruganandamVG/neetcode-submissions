class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*n
        def mincost(index):
            if index>=n:
                return 0
            if dp[index]!=-1:
                return dp[index]
            dp[index]=cost[index]+min(mincost(index+1),mincost(index+2))
            return dp[index]
        return min(mincost(0),mincost(1))
        