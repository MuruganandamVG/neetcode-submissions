class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        n=len(s)
        def checkPalindrome(left,right,s):
            while(left<=right):
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        for i in range(n):
            for j in range(i,n):
                if checkPalindrome(i,j,s):
                    if (j-i+1)>len(longest):
                        longest=s[i:j+1]
        return longest
        