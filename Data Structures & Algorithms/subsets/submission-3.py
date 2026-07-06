class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       ans=[]
       n=len(nums)

       def backtrack(index,subset):
        if index>=n:
            ans.append(subset.copy())
            return 
        subset.append(nums[index])
        backtrack(index+1,subset)
        subset.pop()
        backtrack(index+1,subset)
       backtrack(0,[])
       return ans
        