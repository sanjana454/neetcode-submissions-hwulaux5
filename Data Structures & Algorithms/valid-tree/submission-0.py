class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # condition 1: must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # build adjacency list
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        # DFS to check connectivity
        def dfs(node, parent):
            
            # if already visited → cycle detected
            if node in visit:
                return False

            visit.add(node)

            # explore neighbors
            for nei in adj[node]:
                if nei == parent:
                    continue  # skip the node we came from

                if not dfs(nei, node):
                    return False

            return True

        # start DFS from node 0
        if not dfs(0, -1):
            return False

        # condition 2: must visit all nodes (connected)
        return len(visit) == n