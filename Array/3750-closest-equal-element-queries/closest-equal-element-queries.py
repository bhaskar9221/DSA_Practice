from collections import defaultdict
import bisect
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        mp = defaultdict(list)
        for i, v in enumerate(nums):
            mp[v].append(i)
        
        res = []
        
        for q in queries:
            val = nums[q]
            arr = mp[val]
            
            if len(arr) == 1:
                res.append(-1)
                continue
            
            pos = bisect.bisect_left(arr, q)
            
            left = arr[pos - 1] if pos > 0 else arr[-1]
            right = arr[pos + 1] if pos < len(arr) - 1 else arr[0]
            
            d1 = abs(q - left)
            d2 = abs(q - right)
            
            d1 = min(d1, n - d1)
            d2 = min(d2, n - d2)
            
            res.append(min(d1, d2))
        
        return res