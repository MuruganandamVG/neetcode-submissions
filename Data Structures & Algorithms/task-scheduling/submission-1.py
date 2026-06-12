class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        # cooldown={}
        # time=0
        # while freq:
        #     available_tasks=[]
        #     for task in freq:
        #         if task not in cooldown or cooldown[task]<=time:
        #             available_tasks.append(task)
        #     if available_tasks:
        #         best_task=max(available_tasks,key=lambda x:freq[x])
        #         freq[best_task]-=1
        #         if freq[best_task]==0:
        #             del freq[best_task]
        #         cooldown[best_task]=time+n+1
        #     time+=1
        # return time
        max_heap=[-count for count in freq.values()]
        heapq.heapify(max_heap)
        q=deque([])
        time=0
        while max_heap or q:
            time+=1
            if max_heap:
                cnt=1+heapq.heappop(max_heap)
                if cnt!=0:
                    q.append((cnt,time+n))
            while q and q[0][1]<=time:
                heapq.heappush(max_heap,q.popleft()[0])
        return time

        