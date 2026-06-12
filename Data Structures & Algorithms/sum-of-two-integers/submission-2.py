class Solution:
    def getSum(self, a: int, b: int) -> int:
        res=0
        carry=0
        mask = 0xFFFFFFFF
        for i in range(32):
            x=(a>>i)&1
            y=(b>>i)&1
            addition=x^y^carry
            carry=(x & y) | (x & carry) | (y & carry)
            res= res | (addition<<i)
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res

        
        
        