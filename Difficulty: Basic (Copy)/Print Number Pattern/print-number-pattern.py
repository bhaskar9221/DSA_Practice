class Solution:
    def printPat(self, n):
        #write code here
        result = []
        
        for row in range(n, 0, -1):
            
            for num in range(n, 0, -1):
                
                for _ in range(row):
                    
                    result.append(num)
                    
            result.append(-1)
        return result