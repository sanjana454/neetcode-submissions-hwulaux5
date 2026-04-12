class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # edge case: empty grid
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()   # keeps track of visited cells
        islands = 0     # number of islands

        # BFS function to explore an island
        def bfs(r, c):
            q = collections.deque()

            # mark starting cell as visited
            visit.add((r, c))
            q.append((r, c))

            # process queue
            while q:
                row, col = q.popleft()

                # explore all 4 directions (down, up, right, left)
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    # compute neighbor cell
                    nr, nc = row + dr, col + dc

                    # check:
                    # 1. within bounds
                    # 2. is land ("1")
                    # 3. not visited yet
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visit):

                        # add to queue and mark visited
                        q.append((nr, nc))
                        visit.add((nr, nc))

        # traverse entire grid
        for r in range(rows):
            for c in range(cols):

                # if it's land and not visited → new island found
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)      # explore entire island
                    islands += 1   # increment count

        return islands