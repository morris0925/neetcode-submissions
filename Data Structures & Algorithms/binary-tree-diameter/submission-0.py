# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Key: 從最下面的節點一路數他底下左邊多少，右邊多少，加起來跟 maxDiameter 比
Diameter = 左 + 右
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 此函數只跑一遍，最後 return
        self.maxD = 0
        self.countLR(root)
        return self.maxD
        
    def countLR(self, root):
        if not root:
            return 0

        left = self.countLR(root.left)
        right = self.countLR(root.right)
        self.maxD = max(self.maxD, left + right)  # 途中邊紀錄最大的 l+r  

        return 1 + max(left, right)   # return 深度給上一層使用



















