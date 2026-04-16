class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Space complexity O(m+n)
        num_rows,num_cols = len(matrix), len(matrix[0])   

        rows_to_zero = num_rows*[False]
        cols_to_zero = num_cols*[False]

        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if matrix[row_idx][col_idx] == 0:
                    rows_to_zero[row_idx] = True
                    cols_to_zero[col_idx] = True
        
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if rows_to_zero[row_idx] or cols_to_zero[col_idx]:
                    matrix[row_idx][col_idx] = 0