import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq=[]
        for point in points:
            [x,y]=point
            heapq.heappush(pq,(-math.sqrt(x**2+y**2),point))
            print(pq)
            if len(pq)>k:
                heapq.heappop(pq)
        print(pq)
        res=[ ele[1] for ele in pq]
        print(res)
        return res
        