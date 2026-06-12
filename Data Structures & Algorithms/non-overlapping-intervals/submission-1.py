class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cnt=1
        n=len(intervals)
        end=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]>=end:
                end=intervals[i][1]
                cnt+=1
        return n-cnt