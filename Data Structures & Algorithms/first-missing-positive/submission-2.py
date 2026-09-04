class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        O(n) -> Time Complexity
        O(n) -> Space Complexity
        Not optimal yet
        """
        
        num_set = set(nums)

        i = 1
        while i in num_set:
            i += 1
        return i