class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l=0
        r=n-1
        while(l<r):
            targetSum=numbers[l]+numbers[r]
            if(targetSum>target):
                r-=1
            elif (targetSum<target):
                l+=1
            else:
                return [l+1,r+1]
        