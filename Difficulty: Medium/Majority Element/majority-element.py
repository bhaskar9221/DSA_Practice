class Solution:
    def majorityElement(self, arr):
        #code here
        target = None
        count = 0
        
        for num in arr:
            
            if count == 0:
                target = num
                
            if target == num:
                count += 1
            
            else:
                count -= 1
        
        
        
        if arr.count(target) > len(arr) // 2:
            return target
        return -1