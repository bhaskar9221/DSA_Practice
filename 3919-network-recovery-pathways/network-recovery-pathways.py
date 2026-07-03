import heapq
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        max_cost = 0
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                if cost > max_cost:
                    max_cost = cost
                    
        def check(min_allowed_cost: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]
            
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                if u == n - 1:
                    return d <= k
                for v, cost in adj[u]:
                    if cost >= min_allowed_cost:
                        if d + cost < dist[v]:
                            dist[v] = d + cost
                            heapq.heappush(pq, (dist[v], v))
            return dist[n - 1] <= k

        low, high = 0, max_cost
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
