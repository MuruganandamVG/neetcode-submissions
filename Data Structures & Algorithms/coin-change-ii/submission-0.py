class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        prev=[1 if val%coins[0]==0 else 0 for val in range(amount+1)]
        for index in range(1,n):
            curr=[0 for _ in range(amount+1)]
            for target in range(amount+1):
                take=0
                if target>=coins[index]:
                    take=curr[target-coins[index]]
                notTake=prev[target]
                curr[target]=take+notTake
            prev=curr
        return prev[amount]