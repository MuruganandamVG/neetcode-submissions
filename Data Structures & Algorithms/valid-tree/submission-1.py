class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList=[[] for _ in range(n)]

        for edge in edges:
            u,v=edge
            adjList[u].append(v)
            adjList[v].append(u)
        Visited=set()
        Visited.add(0)
        val=self.dfs(0,-1,Visited,adjList)
        return val and len(Visited)==n

    def dfs(self,node,parent,Visited,adjList):

        
        for vertex in adjList[node]:
            if vertex not in Visited:
                Visited.add(vertex)
                if not self.dfs(vertex,node,Visited,adjList):
                    return False
            elif parent!=vertex:
                return False
        return True
        


        