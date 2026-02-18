class Solution:
    def countDigits(self, n):
    #  code here 
        count = 0
        
        if n == 0:
            return 1
        
        while n != 0:
            n = n // 10
            count += 1
        
        return count