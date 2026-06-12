class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        maxWater=0
        while(left<right):
            water=min(heights[left],heights[right])*(right-left)
            maxWater=max(maxWater,water)
            if heights[left]<=heights[right]:
                left+=1
            elif heights[right]<heights[left]:
                right-=1
        return maxWater


        