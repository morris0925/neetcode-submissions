# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: #如果樹已經走完都還沒找到
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #檢查左右樹是否有機會，True or False >> True
            
        
    
    def sameTree(self, root, subroot):
        if not root and not subroot:
            return True
        
        if (root and subroot) and (root.val == subroot.val):
            left = self.sameTree(root.left, subroot.left)
            right = self.sameTree(root.right, subroot.right)
            return left and right
        
        return False