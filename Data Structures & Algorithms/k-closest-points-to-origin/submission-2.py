import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # # max Heap
        # pq=[]
        # for point in points:
        #     [x,y]=point
        #     heapq.heappush(pq,(-math.sqrt(x**2+y**2),point))
        #     if len(pq)>k:
        #         heapq.heappop(pq)
        # res=[ ele[1] for ele in pq]
        # return res

        # MinHeap
        minHeap=[]
        for point in points:
            [x,y]=point
            minHeap.append((x**2+y**2,point))
        heapq.heapify(minHeap)
        res=[]
        while(k>0):
            [dist,point]=heapq.heappop(minHeap)
            res.append(point)
            k-=1
        return res
        