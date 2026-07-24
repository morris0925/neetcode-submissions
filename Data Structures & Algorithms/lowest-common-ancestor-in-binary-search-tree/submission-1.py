# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Key Pattern to Observe: BST 左邊比較小 右邊比較大
        1. 一左一右、其中一個是本身: LCA = 自己 (base case)
        2. 全部都在左邊: 往左走，直到遇到一左一右或其中一個是本身，找到LCA
        3. 全部都在右邊: 往右走，直到遇到一左一右或其中一個是本身，找到LCA
        """
        curr = root
        
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
                

