class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        component = [0] * n
        curr_id = 0
        
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                curr_id += 1
            component[i] = curr_id
            
        return [component[u] == component[v] for u, v in queries]
