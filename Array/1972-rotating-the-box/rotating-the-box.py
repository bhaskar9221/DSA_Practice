class Solution:
    def rotateTheBox(self, box):
        m, n = len(box), len(box[0])

        for row in box:
            empty = n - 1

            for j in range(n - 1, -1, -1):

                if row[j] == '*':
                    empty = j - 1

                elif row[j] == '#':
                    row[j], row[empty] = '.', '#'
                    empty -= 1

        res = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = box[i][j]

        return res