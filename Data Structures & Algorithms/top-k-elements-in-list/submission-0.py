class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter={}
        n=len(nums)
        for i in range(n):
            freqCounter[nums[i]]=1+freqCounter.get(nums[i],0)
        topKeys=sorted(freqCounter,key=freqCounter.get,reverse=True)[:k]
        return topKeys
        