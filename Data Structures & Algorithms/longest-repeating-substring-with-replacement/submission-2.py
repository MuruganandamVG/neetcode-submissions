class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength=0;
        n=len(s)
        for i in range(n):
            hashMap={}
            maxCount=0
            for j in range(i,n):
                hashMap[s[j]]=1+hashMap.get(s[j],0)
                maxCount=max(hashMap[s[j]],maxCount)
                strLength=j-i+1
                if (strLength-maxCount<=k):
                    maxLength=max(maxLength,strLength)
        return maxLength




        