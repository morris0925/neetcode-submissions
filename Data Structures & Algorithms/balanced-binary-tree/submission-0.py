# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.maxGap = 0
        self.check(root)
        if self.maxGap > 1:
            return False
        else:
            return True


    def check(self, root):
        if not root:
            return 0

        left = self.check(root.left)
        right = self.check(root.right)
        self.maxGap = max(self.maxGap, left - right, right - left)

        return 1 + max(left, right)

        



        