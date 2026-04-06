class Solution:
    def segregate0and1(self, arr):
        # code here
        zero = arr.count(0)
        ones = [i for i in arr if i>0]
        arr[:] = [0]*zero + ones
        return arr