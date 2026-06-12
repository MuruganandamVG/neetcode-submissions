class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        x=s.lower()
        left,right=0,n-1
        while left<right:
            while left<right and not x[left].isalnum():
                left+=1
            while left<right and not x[right].isalnum():
                right-=1
            if x[left]!=x[right]:
                return False
            left+=1
            right-=1
        return True

        