#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        n_backup = n
        power = len(str(n))
        total_sum = 0
        
        while n>0:
            digit = n%10
            total_sum = total_sum + digit**power
            n //= 10
        return total_sum == n_backup