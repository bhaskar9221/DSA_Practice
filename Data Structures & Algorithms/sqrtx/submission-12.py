class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        if x<2: return x

        while left <= right:
            mid = (left + right) // 2

            if mid <= x // mid:
                left = mid + 1
            else:
                right = mid - 1

        return right