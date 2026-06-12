class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def maxMoney(index):
            if index>=n:
                return 0
            if dp[index]!=-1:
                return dp[index]
            dp[index]=max(nums[index]+maxMoney(index+2),maxMoney(index+1))
            return dp[index]
        return maxMoney(0)

        