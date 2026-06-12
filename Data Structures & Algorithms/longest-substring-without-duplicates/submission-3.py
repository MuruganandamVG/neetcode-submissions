class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0;
        n=len(s)
        if n==0:
            return n
        left,right=0,0
        hashChar={}
        while(right<n):
            if s[right] in hashChar:
                left=max(left,hashChar[s[right]]+1)
            maxLength=max(maxLength,right-left+1)
            hashChar[s[right]]=right
            right+=1
        return maxLength


        