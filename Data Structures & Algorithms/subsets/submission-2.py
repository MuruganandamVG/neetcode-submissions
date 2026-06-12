class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def generate(start,path):
            res.append(path.copy())
            for i in range(start,n):
                generate(i+1,path+[nums[i]])
        generate(0,[])
        return res
        