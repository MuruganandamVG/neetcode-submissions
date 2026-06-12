class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins=float('-inf')
        dp={}
        def findCoins(target):
            if target<0:
                return float('inf');
            if target==0:
                return 0
            if target in dp:
                return dp[target]
            minVal=float('inf')
            for i in range(len(coins)):
                minVal=min(1+findCoins(target-coins[i]),minVal)
            dp[target]= minVal
            return dp[target]
        res=findCoins(amount)
        return res if res!=float('inf') else -1



        