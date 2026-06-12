class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def noofsteps(index):
            if index<=1:
                return 1
            if dp[index]!=-1:
                return dp[index]
            onestep=noofsteps(index-1)
            twosteps=noofsteps(index-2)
            dp[index]=onestep+twosteps
            return dp[index]
        return noofsteps(n)