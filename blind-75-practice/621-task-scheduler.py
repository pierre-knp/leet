from typing import List
import collections, heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        maxHeap =[-count for count in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = collections.deque()
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))
                    
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time

sol = Solution()

print(sol.leastInterval(["A","C","A","B","D","B"], n = 1))