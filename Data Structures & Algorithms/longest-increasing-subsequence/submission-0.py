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
        temp=[]
        temp.append(nums[0])
        n=len(nums)
        for i in range(1,n):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                index=self.getIndex(temp,nums[i])
                temp[index]=nums[i]
        return len(temp)


        