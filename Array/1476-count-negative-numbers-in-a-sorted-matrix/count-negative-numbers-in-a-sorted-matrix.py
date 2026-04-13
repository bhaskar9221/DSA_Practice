class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for element in grid:
            element.sort()

            count += bisect_left(element, 0)
        return count