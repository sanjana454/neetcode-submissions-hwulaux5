class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pac, atl = set(), set()  # reachable cells

        # DFS function
        def dfs(r, c, visit, prevHeight):
            
            # stop if out of bounds OR already visited OR invalid height flow
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit or
                heights[r][c] < prevHeight):
                return

            # mark cell as reachable
            visit.add((r, c))

            # explore all 4 directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # run DFS from Pacific (top row + left column)
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])         # top edge
            dfs(rows - 1, c, atl, heights[rows - 1][c])  # bottom edge

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])         # left edge
            dfs(r, cols - 1, atl, heights[r][cols - 1])  # right edge

        # find cells reachable by both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res