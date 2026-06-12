class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n=len(nums)
        total=sum(nums)
        req=total-target
        if (req<0 or req%2!=0):
            return 0
        target=req//2
        prev=[0 for _ in range(target+1)]
        if nums[0]==0:
            prev[0]=2
        else:
            prev[0]=1
            if nums[0]<=target:
                prev[nums[0]]=1
        for i in range(1,n):
            curr=[0 for _ in range(target+1)]
            for val in range(target+1):
                take=0
                if val>=nums[i]:
                    take=prev[val-nums[i]]
                notTake=prev[val]
                curr[val]=take+notTake
            prev=curr
        return prev[target]
