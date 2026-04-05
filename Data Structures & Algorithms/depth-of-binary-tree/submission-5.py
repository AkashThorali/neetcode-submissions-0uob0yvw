# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque()
        level = 0

        q.append(root)
        while q: 
            elements = len(q)
            for i in range(elements):
                item = q.popleft()
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            level += 1
        return level


        