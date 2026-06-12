class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        cooldown={}
        time=0
        while freq:
            available_tasks=[]
            for task in freq:
                if task not in cooldown or cooldown[task]<=time:
                    available_tasks.append(task)
            if available_tasks:
                best_task=max(available_tasks,key=lambda x:freq[x])
                freq[best_task]-=1
                if freq[best_task]==0:
                    del freq[best_task]
                cooldown[best_task]=time+n+1
            time+=1
        return time
        