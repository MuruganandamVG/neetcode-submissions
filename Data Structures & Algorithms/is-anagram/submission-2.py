class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for ch in t:
            if ch in s:
                s=s.replace(ch,"",1)
            else:
                return False
        print(s)
      
        return len(s)==0
        