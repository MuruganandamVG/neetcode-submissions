class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n=len(nums)
        res=set()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                target=nums[left]+nums[right]+nums[i]
                if target<0:
                    left+=1
                elif target>0:
                    right-=1
                else:
                    res.add((nums[left],nums[right],nums[i]))
                    left+=1
                    right-=1
                    # while left<right and nums[left]==nums[left-1]:
                    #     left+=1
                    # while left<right and nums[right]==nums[right+1]:
                    #     right-=1
        return [list(ele) for ele in res]


       