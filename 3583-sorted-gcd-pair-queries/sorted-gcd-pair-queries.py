from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        exact = [0] * (mx + 1)

        # Process from large gcd to small gcd
        for g in range(mx, 0, -1):
            cnt = 0
            for m in range(g, mx + 1, g):
                cnt += freq[m]

            exact[g] = cnt * (cnt - 1) // 2

            for m in range(2 * g, mx + 1, g):
                exact[g] -= exact[m]

        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))

        return ans