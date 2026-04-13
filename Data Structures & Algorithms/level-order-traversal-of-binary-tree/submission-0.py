# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# running a bfs and add it to a list level by level 
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []  # final result: list of levels

        # edge case: if tree is empty
        if not root:
            return res

        q = deque()
        q.append(root)  # start BFS with root node

        # BFS traversal
        while q:

            qlen = len(q)   # number of nodes in current level
            level = []      # store values for this level

            # process all nodes in current level
            for i in range(qlen):

                node = q.popleft()  # remove node from queue

                # add node value to current level
                level.append(node.val)

                # add children to queue for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # after finishing this level, add it to result
            res.append(level)

        return res