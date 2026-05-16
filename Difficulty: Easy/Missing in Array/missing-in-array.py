class Solution:
    def missingNum(self, arr):
        # code heree
        n = len(arr)+1
        
        sumN = (n*(n+1))//2
        
        return sumN-sum(arr)