class Solution:
    def maxSubarraySum(self, nums):
        # Code here
        current_sum = 0
        max_sum = nums[0]

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0
        return max_sum