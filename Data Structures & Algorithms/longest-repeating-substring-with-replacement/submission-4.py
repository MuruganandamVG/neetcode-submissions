class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        left,right=0,0
        chars=defaultdict(int)
        maxFreq=0
        maxWindow=0
        while right<n:
            chars[s[right]]+=1
            maxFreq=max(maxFreq,chars[s[right]])
            while (((right-left+1)-maxFreq))>k:
                chars[s[left]]-=1
                left+=1
            maxWindow=max(maxWindow,right-left+1)
            right+=1
        return maxWindow
            

        