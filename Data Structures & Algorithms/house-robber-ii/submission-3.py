class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return max(nums)
        def maxAmount(arr):
            n=len(arr)
            dp=[0]*(n)
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            for i in range(2,n):
                dp[i]=max(arr[i]+dp[i-2],dp[i-1])
            return dp[-1]
        return max(maxAmount(nums[:n-1]),maxAmount(nums[1:n]))
        