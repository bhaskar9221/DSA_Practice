class Solution:
    def mirrorDistance(self, n: int) -> int:

        def reversing_n(n):
            reversed_n = 0
            while n:
                digit = n%10
                reversed_n = reversed_n*10 + digit
                n //= 10
            return reversed_n
        
        return abs(n - reversing_n(n))