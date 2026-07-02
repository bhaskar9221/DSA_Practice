from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                idx = bisect_left(matrix[i], target)
                return idx < m and matrix[i][idx] == target
        return False