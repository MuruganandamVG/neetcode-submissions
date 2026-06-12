class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while(len(stones)>1):
            stones.sort()
            a=stones.pop()
            b=stones.pop()
            if a!=b:
                stones.append(abs(b-a))
        return stones[0] if len(stones) else 0

        