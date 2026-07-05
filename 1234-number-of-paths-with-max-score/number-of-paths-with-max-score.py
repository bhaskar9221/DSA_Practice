class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == n - 1 and c == n - 1:
                    continue
                if board[r][c] == 'X':
                    continue

                max_score, paths = -1, 0
                curr_val = 0 if board[r][c] == 'E' else int(board[r][c])

                for dr, dc in [(0, 1), (1, 0), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < n and nc < n and dp[nr][nc][0] != -1:
                        score = dp[nr][nc][0] + curr_val
                        if score > max_score:
                            max_score = score
                            paths = dp[nr][nc][1]
                        elif score == max_score:
                            paths = (paths + dp[nr][nc][1]) % MOD

                if max_score != -1:
                    dp[r][c] = [max_score, paths]

        ans = dp[0][0]
        return ans if ans[0] != -1 else [0, 0]