class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Using Maths Formula for Sum or N Natural Numbers
        array_sum = sum(nums)
        n = len(nums)
        sum_n = n * (n+1) // 2

        return sum_n - array_sum