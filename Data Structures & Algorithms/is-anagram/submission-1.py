class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount={}
        for i in range(len(s)):
            if s[i] not in charCount:
                charCount[s[i]]=1
            else:
                charCount[s[i]]+=1
        for i in range(len(t)):
            if t[i] in charCount:
                charCount[t[i]]-=1
            else:
                return False
        for key,val in charCount.items():
            if(val!=0):
                return False
        return True
        