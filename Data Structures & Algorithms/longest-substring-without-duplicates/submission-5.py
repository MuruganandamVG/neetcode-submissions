class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique=set()
        n=len(s)
        left,right=0,0
        maxLen=0
        while right<n:
            while s[right] in unique:
                unique.remove(s[left])
                left+=1
            unique.add(s[right])
            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen

