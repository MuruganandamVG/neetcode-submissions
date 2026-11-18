class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList=[[]*n for _ in range(n)]
        for edge in edges:
            u,v=edge
            adjList[u].append(v)
            adjList[v].append(u)
        connected=0
        visited=[False]*n
        for i in range(len(visited)):
            if not visited[i]:
                self.bfs(i,n,adjList,visited)
                connected+=1
        return connected
    def bfs(self,node,n,adjList,visited):
        q=deque([node])
        while q:
            n=len(q);
            for i in range(n):
                node=q.popleft()
                visited[node]=True
                for vertex in adjList[node]:
                    if not visited[vertex]:
                        q.append(vertex)
                        visited[vertex]=True
            


        