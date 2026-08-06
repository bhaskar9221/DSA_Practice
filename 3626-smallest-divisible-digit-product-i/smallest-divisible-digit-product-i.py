class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        from itertools import count
      
        for candidate in count(n):
            digit_product = 1
            temp_num = candidate
          
            while temp_num > 0:
                digit = temp_num % 10  
                digit_product *= digit  
                temp_num //= 10  
          
            if digit_product % t == 0:
                return candidate