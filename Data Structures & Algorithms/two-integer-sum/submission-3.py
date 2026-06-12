class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            required=target-nums[i]
            if required in hashMap:
                return[hashMap.get(required),i]
            hashMap[nums[i]]=i
       
        