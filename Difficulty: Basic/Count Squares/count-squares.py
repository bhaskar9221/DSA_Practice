#User function Template for python3

class Solution:
    def countSquares(self, n):
        # code here 
        num = n ** 0.5
        new = int(num)
        diff = num-new
        if(diff>0):
            return new
        elif(diff==0):
            return new-1