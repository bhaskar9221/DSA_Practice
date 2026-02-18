class Solution:
    def reverse(self, n: int) -> int:
        rev = 0
        sign = -1 if n < 0 else 1   # store sign
        n = abs(n)                  # make it positive

        while n > 0:
            a = n % 10
            rev = rev * 10 + a
            n = n // 10
        result = rev * sign 
        if result <-2**31 or result > 2**31 - 1:
            return 0
        return result