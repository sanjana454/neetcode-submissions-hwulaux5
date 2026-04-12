class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # build adjacency list
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        components = 0

        # DFS to visit all nodes in one component
        def dfs(node):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        # check every node
        for i in range(n):

            # if node not visited → new component found
            if i not in visited:
                dfs(i)
                components += 1

        return components