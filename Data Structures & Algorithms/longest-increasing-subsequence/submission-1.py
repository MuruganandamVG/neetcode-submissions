from bisect import bisect_left
class Solution:
    def getIndex(self,arr,target):
        left,right=0,len(arr)-1
        index=0
        while left<=right:
            mid=(left+right)//2 
            if arr[mid]>=target:
                index=mid
                right=mid-1
            else:
                left=mid+1
        return index
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        dp.append(nums[0])
        n=len(nums)
        LIS=1
        for i in range(1,n):
            if nums[i]>dp[-1]:
                dp.append(nums[i])
                LIS+=1
            else:
                index=bisect_left(dp,nums[i])
                dp[index]=nums[i]
        return LIS


        