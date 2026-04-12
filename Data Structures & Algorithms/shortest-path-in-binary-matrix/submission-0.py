from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        
        n = len(grid)

        # if start or end is blocked → no path
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # 8 possible movements (including diagonals)
        directions = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]

        # BFS queue: (row, col, distance so far)
        q = deque()
        q.append((0, 0, 1))  # start distance = 1

        visited = set()
        visited.add((0, 0))

        while q:
            r, c, dist = q.popleft()

            # if we reached destination → return shortest path
            if r == n - 1 and c == n - 1:
                return dist

            # explore all 8 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # check valid cell
                if (0 <= nr < n and 0 <= nc < n and
                    grid[nr][nc] == 0 and
                    (nr, nc) not in visited):

                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))

        # if queue empties → no path exists
        return -1