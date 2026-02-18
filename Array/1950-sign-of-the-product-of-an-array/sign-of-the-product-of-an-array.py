class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Optimal Solution = Counting the number of +ve, -ve and 0 elements
        sign = 1

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign *= -1
        return sign