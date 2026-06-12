class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[-1]*n
        def func(index):
            if index==n:
                return True 
            if dp[index]!=-1:
                return dp[index]
            string=""
            res=False
            for j in range(index,n):
                string+=s[j]
                if string in wordDict:
                    res =res or func(j+1)
            dp[index]=res
            return dp[index]
        return func(0)
        