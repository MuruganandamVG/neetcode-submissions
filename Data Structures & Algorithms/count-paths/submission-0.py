class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def countPaths(i,j):
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            up=countPaths(i-1,j)
            left=countPaths(i,j-1)
            return up+left
        return countPaths(m-1,n-1)