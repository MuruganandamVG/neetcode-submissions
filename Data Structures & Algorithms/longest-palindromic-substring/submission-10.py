class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        n=len(s)
        dp=[[-1]*n for _ in range(n)]
        def checkPalindrome(left,right):
            if left>=right:
                return True 
            if dp[left][right]!=-1:
                return dp[left][right]
            if s[left]==s[right]:
                dp[left][right]=checkPalindrome(left+1,right-1)
            else:
                dp[left][right]=False   
            return dp[left][right] 
        for i in range(n):
            for j in range(i,n):
                if checkPalindrome(i,j):
                    if (j-i+1)>len(longest):
                        longest=s[i:j+1]
        return longest
        