class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        target=sum(nums)
        if target%2!=0:
            return False 
        target=target//2
        prev=[True if nums[0]==val else False for val in range(target+1)]
        for i in range(1,n):
            curr=[False for _ in range(target+1)]
            curr[0]=True 
            for j in range(1,target+1):
                take=False 
                if j>=nums[i]:
                    take=prev[j-nums[i]]
                notTake=prev[j]
                curr[j]=take or notTake 
            prev=curr 
        return prev[target]
        