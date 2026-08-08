from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        Initialize the data structure with a 2D matrix.
        Build a 2D prefix sum array for efficient range sum queries.
      
        Args:
            matrix: 2D list of integers
        """
        rows, cols = len(matrix), len(matrix[0])
      
        # Create prefix sum array with extra row and column of zeros for easier calculation
        # prefix_sum[i][j] represents the sum of all elements from (0,0) to (i-1,j-1)
        self.prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
      
        # Build the prefix sum array
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                # Current prefix sum = sum above + sum to the left - overlap + current value
                self.prefix_sum[i + 1][j + 1] = (
                    self.prefix_sum[i][j + 1] +      # Sum of rectangle above
                    self.prefix_sum[i + 1][j] -      # Sum of rectangle to the left
                    self.prefix_sum[i][j] +          # Remove double-counted overlap
                    value                            # Add current cell value
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Calculate the sum of elements in the rectangle defined by its corners.
      
        Args:
            row1: Top row index (inclusive)
            col1: Left column index (inclusive)
            row2: Bottom row index (inclusive)
            col2: Right column index (inclusive)
          
        Returns:
            Sum of all elements in the specified rectangle
        """
        # Use inclusion-exclusion principle to get the rectangle sum
        return (
            self.prefix_sum[row2 + 1][col2 + 1] -    # Total sum from origin to bottom-right
            self.prefix_sum[row2 + 1][col1] -        # Subtract left rectangle
            self.prefix_sum[row1][col2 + 1] +        # Subtract top rectangle
            self.prefix_sum[row1][col1]              # Add back double-subtracted overlap
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1, col1, row2, col2)
