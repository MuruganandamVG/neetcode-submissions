class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftMaxHeights=[0]*n
        leftMaxHeights[0]=height[0]
        rightMaxHeights=[0]*n
        rightMaxHeights[n-1]=height[n-1]
        for i in range(1,n):
            leftMaxHeights[i]=max(height[i],leftMaxHeights[i-1])
        for i in range(n-2,-1,-1):
            rightMaxHeights[i]=max(height[i],rightMaxHeights[i+1])
        res=0
        for i in range(1,n-1):
            res+=min(leftMaxHeights[i],rightMaxHeights[i])-height[i]
        return res

        