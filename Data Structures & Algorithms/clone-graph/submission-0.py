"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNew={}
        return self.dfs(node,oldNew) if node else None

    def dfs(self,node,oldNew):
        if node in oldNew:
            return oldNew[node]
        copy=Node(node.val)
        oldNew[node]=copy
        for neigh in node.neighbors:
            copy.neighbors.append(self.dfs(neigh,oldNew))
        return copy
    
        