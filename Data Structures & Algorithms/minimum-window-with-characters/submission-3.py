class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        hashArray=[0]*256
        for ch in t:
            hashArray[ord(ch)]+=1
        left,right=0,0
        cnt=0
        minStr=""
        minLength=float('inf')
        while right<n:
            if hashArray[ord(s[right])]>0:
                cnt+=1
            hashArray[ord(s[right])]-=1
            while cnt==len(t):
                if (right-left+1)<minLength:
                    minLength=right-left+1
                    minStr=s[left:right+1]
                hashArray[ord(s[left])]+=1
                if hashArray[ord(s[left])]>0:
                    cnt-=1
                left+=1
            right+=1
        return minStr
            
        