# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        res = []
        queue = deque([root])

        while queue: 
            number_of_nodes = len(queue)
            nodes = []

            for i in range(number_of_nodes):
                node = queue.popleft()
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            res.append(nodes)

        return res



