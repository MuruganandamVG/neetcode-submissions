class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        actualSum=(n*(n+1))/2
        return int(actualSum -sum(nums))
        