class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        from functools import cache
        from math import inf
      
        @cache
        def dfs(current_index: int) -> int:
            if current_index == array_length - 1:
                return 0
          
            max_jumps = -inf
          
            for next_index in range(current_index + 1, array_length):
                if abs(nums[current_index] - nums[next_index]) <= target:
                    max_jumps = max(max_jumps, 1 + dfs(next_index))
          
            return max_jumps
      
        array_length = len(nums)
      
        result = dfs(0)
      
        return -1 if result < 0 else result
