class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # dp[r][c] = number of ways to reach cell (r, c)
        dp = [[1] * n for _ in range(m)]

        # first row and first column are always 1
        # (only one way: keep moving right or down)

        for r in range(1, m):
            for c in range(1, n):

                # number of ways = from top + from left
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        # bottom-right corner is the answer
        return dp[m-1][n-1]