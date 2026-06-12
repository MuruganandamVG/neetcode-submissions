class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp=[[-1 for _ in range(n)] for _ in range(m)]
        
        def countPaths(i,j):
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            up=countPaths(i-1,j)
            left=countPaths(i,j-1)
            dp[i][j]=up+left
            return dp[i][j]
        return countPaths(m-1,n-1)