class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def generate(s,open,close):
            if open==n and close==n:
                res.append(s)
                return ;
            if(open<n):
                generate(s+'(',open+1,close)
            if(close<open):
               generate(s+')',open,close+1)
        generate("(",1,0)
        return res
        