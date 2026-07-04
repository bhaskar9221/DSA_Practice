class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        ans = float("inf")
        visited = {1}
        q = deque([1])

        while q:
            u = q.popleft()
            for v, d in graph[u]:
                ans = min(ans, d)
                if v not in visited:
                    visited.add(v)
                    q.append(v)

        return ans