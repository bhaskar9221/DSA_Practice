class Solution:
    def findEquilibrium(self, arr):
        # code here

        sum, curr_sum =0,0
        
        for x in arr:
            sum+=x
            
        
        for i in range(len(arr)):
            
            if sum-arr[i] == 2*curr_sum:
               return i
            
            curr_sum+= arr[i]
        
        
        
        return -1