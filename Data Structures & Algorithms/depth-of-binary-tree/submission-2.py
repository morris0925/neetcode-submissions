# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS iterative approach

        if not root:
            return 0

        stack = [[root, 1]]
        result = 1

        while stack:
            node, layer = stack.pop()
            if node.left:
                stack.append([node.left, layer + 1])
                result = max(result, layer + 1)
            if node.right:
                stack.append([node.right, layer + 1])
                result = max(result, layer + 1)
        
        return result





