
class Solution:
    def guessNumber(self, n: int) -> int:
        i,j = 0,n
        
        while i<=j:
            mid = (i+j)//2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                j = mid - 1
            else:
                i = mid + 1
                