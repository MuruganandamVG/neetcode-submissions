from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count=0
        rows=len(grid)
        cols=len(grid[0])
        Visited=[[False]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if not Visited[i][j] and grid[i][j]=="1":
                    count+=1
                    self.bfs(i,j,grid,Visited,rows,cols)
        return count



    def isValid(self,r,c,rows,cols):
        if r<0 or c<0 or r>=rows or c>=cols:
            return False
        return True



    def bfs(self,row,col,grid,Visited,m,k):
        q=deque([(row,col)])
        Visited[row][col]=True
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                r,c=node
                for dr,dc in directions:
                        nRow=r+dr
                        nCol=c+dc
                        if self.isValid(nRow,nCol,m,k) and not Visited[nRow][nCol] and grid[nRow][nCol]=="1":
                            Visited[nRow][nCol]=True
                            q.append((nRow,nCol))

        