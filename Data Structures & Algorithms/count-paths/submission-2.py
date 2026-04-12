class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # row[j] represents number of ways to reach destination
        # from cell in current row at column j
        # initialize last row: all 1s (only one way to go right)
        row = [1] * n

        # iterate from second last row up to first row
        for i in range(m - 1):

            # newrow will store DP values for the current row
            # initialize it as 1s (last column is always 1 way going down)
            newrow = [1] * n

            # fill from right to left (bottom-up dependency)
            for j in range(n - 2, -1, -1):

                # recurrence:
                # ways = right cell + cell below (from previous row)
                newrow[j] = newrow[j + 1] + row[j]

            # move current row up for next iteration
            row = newrow

        # top-left cell contains final answer
        return row[0]