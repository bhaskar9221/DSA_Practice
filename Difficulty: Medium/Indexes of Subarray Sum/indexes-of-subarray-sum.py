class Solution:
    def subarraySum(self, arr, target):
        first = 0
        current_sum = 0
        
        for last in range(len(arr)):
            current_sum += arr[last]
            
            while current_sum > target and first <= last:
                current_sum -= arr[first]
                first += 1
                
            if current_sum == target:
                return (first + 1, last + 1)
        
        return (-1,)