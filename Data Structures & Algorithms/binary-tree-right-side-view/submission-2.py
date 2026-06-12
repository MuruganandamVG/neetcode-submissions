# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # res=[]
        # if not root:
        #     return []
        # q=deque([root])
        # while(q):
        #     rightSide=None
        #     for i in range(len(q)):
        #         node=q.popleft()
        #         rightSide=node
        #         if (node.left):
        #             q.append(node.left)
        #         if (node.right):
        #             q.append(node.right)
        #     res.append(rightSide.val)
        # return res
        res=[]
        def dfs(depth,node):
            if node is None:
                return 
            if depth==len(res):
                res.append(node.val)
            dfs(depth+1,node.right)
            dfs(depth+1,node.left)
        if not root:
            return res
        dfs(0,root)
        return res
        
        