class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength=0;
        left,right=0,0
        hashMap={}
        n=len(s)
        maxCount=0;
        while(right<n):
            hashMap[s[right]]=hashMap.get(s[right],0)+1
            maxCount=max(maxCount,hashMap[s[right]])
            while((right-left+1)-maxCount>k):
                hashMap[s[left]]-=1
                localMax=0;
                for val in hashMap.values():
                    localMax=max(localMax,val)
                maxCount=localMax
                left+=1
            maxLength=max(maxLength,right-left+1)
            right+=1
        return maxLength




        