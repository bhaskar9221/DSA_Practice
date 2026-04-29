class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_triangle = []

        for n in range(numRows):
            row=[1]
            val = 1

            for r in range(1,n+1):
                val = val*(n-r+1)//r
                row.append(val)
            final_triangle.append(row)
        return final_triangle