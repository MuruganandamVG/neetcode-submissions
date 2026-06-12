class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        n=len(s)
        for i in range(n):
            palindrome=""
            for j in range(i,n):
                palindrome+=s[j]
                if palindrome==palindrome[::-1]:
                    if len(palindrome)>len(longest):
                        longest=palindrome
        return longest
        