class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_map = set(nums)
        result = 0

        for num in nums_map:
            if num-1 not in nums_map:
                current_length, current_num = 0, num

                while current_num in nums_map:
                    current_length += 1
                    current_num += 1

                result = max(result,current_length)
        return result