"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # hashmap to store mapping:
        # original node → cloned node
        # helps avoid re-creating nodes and handles cycles
        oldtonew = {}

        def dfs(node):
            
            # if node already cloned, return its copy
            # prevents infinite loops in cyclic graphs
            if node in oldtonew:
                return oldtonew[node]

            # create a copy of current node
            copy = Node(node.val)

            # store mapping before exploring neighbors
            # IMPORTANT: avoids infinite recursion
            oldtonew[node] = copy

            # iterate through neighbors
            for n in node.neighbors:
                
                # recursively clone neighbors
                # and connect them to current copied node
                copy.neighbors.append(dfs(n))

            # return cloned node
            return copy

        # handle empty graph
        return dfs(node) if node else None