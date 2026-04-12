class Solution:
    def calcEquation(self, equations, values, queries):
        
        # build graph
        graph = {}

        for (a, b), val in zip(equations, values):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            # a / b = val
            graph[a].append((b, val))
            # b / a = 1/val
            graph[b].append((a, 1 / val))

        # DFS to evaluate path
        def dfs(src, target, visited):
            
            # if node missing
            if src not in graph:
                return -1.0

            # reached target
            if src == target:
                return 1.0

            visited.add(src)

            for nei, weight in graph[src]:
                if nei in visited:
                    continue

                result = dfs(nei, target, visited)

                if result != -1.0:
                    return weight * result

            return -1.0

        # answer each query
        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))

        return res