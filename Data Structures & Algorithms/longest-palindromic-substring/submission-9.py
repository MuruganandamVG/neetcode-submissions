class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        n=len(s)
        def checkPalindrome(left,right):
            if left>=right:
                return True 
            if s[left]==s[right]:
                return checkPalindrome(left+1,right-1)
            return False    
        for i in range(n):
            for j in range(i,n):
                if checkPalindrome(i,j):
                    if (j-i+1)>len(longest):
                        longest=s[i:j+1]
        return longest
        