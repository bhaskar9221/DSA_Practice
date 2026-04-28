class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        minimum_operations = 0
        flatten_grid = []
        reference_remainder = grid[0][0]%x

        for row in grid:
            for value in row:
                if value%x != reference_remainder:
                    return -1
                flatten_grid.append(value)
        flatten_grid.sort()

        median_index = len(flatten_grid)//2
        median_value = flatten_grid[median_index]

        minimum_operations = sum(abs(value-median_value)//x for value in flatten_grid)
        return minimum_operations