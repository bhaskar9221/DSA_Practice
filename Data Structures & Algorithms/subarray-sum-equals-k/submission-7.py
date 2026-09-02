class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        current_sum = 0
        seen = {0:1}

        for num in nums:
            current_sum += num
            difference = current_sum - k

            result += seen.get(difference,0)
            seen[current_sum] = 1 + seen.get(current_sum,0)
        return result