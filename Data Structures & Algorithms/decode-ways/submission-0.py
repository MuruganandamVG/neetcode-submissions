class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        decode_map={str(i):chr(64+i) for i in range(1,27)}
        dp=[-1]*n
        def decodeWays(index):
            if index==n:
                return 1
            if dp[index]!=-1:
                return dp[index]
            oneStr=0
            if s[index] in decode_map:
                oneStr=decodeWays(index+1)
            twoStr=0
            if index+1<n and s[index:index+2] in decode_map:
                twoStr=decodeWays(index+2)
            dp[index]=oneStr+twoStr
            return dp[index]
        return decodeWays(0)
        
        