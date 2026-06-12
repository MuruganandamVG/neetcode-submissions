class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        maxLength=0
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        dp=[[-1]*m for _ in range(n)]
        def strictlyIncreasing(row,col):
            if dp[row][col]!=-1:
                return dp[row][col]
            length=1
            for [dr,dc] in directions:
                x,y=row+dr,col+dc
                if 0<=x<n and 0<=y<m and matrix[x][y]>matrix[row][col]:
                    length=max(1+strictlyIncreasing(x,y),length)
            dp[row][col]=length
            return dp[row][col]
        for row in range(n):
            for col in range(m):
                if(strictlyIncreasing(row,col)):
                    maxLength=max(maxLength,strictlyIncreasing(row,col))
        return maxLength
        