class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = current_sum = 0
        seen = {0:1}

        for num in nums:
            current_sum += num
            difference = current_sum - k

            count += seen.get(difference,0)
            seen[current_sum] = seen.get(current_sum,0) + 1
        return count