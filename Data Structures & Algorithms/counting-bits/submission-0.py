class Solution:
    def countBits(self, n: int) -> List[int]:

        def countsetBits(num):
            count=0
            while num:
                num=num&(num-1)
                count+=1
            return count
        res=[0]
        for i in range(1,n+1):
            res.append(countsetBits(i))
        return res

        