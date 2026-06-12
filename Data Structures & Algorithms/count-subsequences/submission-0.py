class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mod=10**9+7
        n=len(s)
        m=len(t)
        dp=[[-1]*m for _ in range(n)]
        def countDistinctSubSequences(i,j,s,t):
            if j<0:
                return 1
            if i<0:
                return 0 
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j]=countDistinctSubSequences(i-1,j-1,s,t)+countDistinctSubSequences(i-1,j,s,t)
            else:
                dp[i][j]=countDistinctSubSequences(i-1,j,s,t)
            return dp[i][j]%mod
        return countDistinctSubSequences(n-1,m-1,s,t)
   
        