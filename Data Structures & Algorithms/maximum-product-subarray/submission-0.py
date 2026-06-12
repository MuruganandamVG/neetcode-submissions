class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSubarrayProduct=nums[0]
        n=len(nums)
        for i in range(n):
            mult=1
            for j in range(i,n):
                mult*=nums[j]
                maxSubarrayProduct=max(maxSubarrayProduct,mult)
        return maxSubarrayProduct

        