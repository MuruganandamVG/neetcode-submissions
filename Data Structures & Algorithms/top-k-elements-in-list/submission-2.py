class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter={}
        n=len(nums)
        res=[]
        for i in range(n):
            freqCounter[nums[i]]=1+freqCounter.get(nums[i],0)
        freqArray=[[] for _ in range(n+1)]
        for key,val in freqCounter.items():
            freqArray[val].append(key)
        for i in range(len(freqArray)-1,-1,-1):
            for j in range(len(freqArray[i])):
                res.append(freqArray[i][j])
        return res[:k]


       
        