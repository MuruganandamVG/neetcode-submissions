class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        n=len(intervals)
        merged=[]
        for i in range(n):
            if not merged or intervals[i][0]>merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1][1]=max(merged[-1][1],intervals[i][1])
        return merged
        