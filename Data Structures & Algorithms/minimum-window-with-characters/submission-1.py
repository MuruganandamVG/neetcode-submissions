class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minStr=''
        minLen=float('inf')
        n=len(s)
        m=len(t)
        for i in range(n):
            hash=[0]*256
            for ch in t:
                hash[ord(ch)]+=1
            cnt=0
            for j in range(i,n):
                if hash[ord(s[j])]>0:
                    cnt+=1
                hash[ord(s[j])]-=1
                if cnt==len(t):
                    if (j-i+1)<minLen:
                        minLen=j-i+1
                        minStr=s[i:j+1]
        return minStr
        