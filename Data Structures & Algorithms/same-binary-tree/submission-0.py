# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # 終點結束情況: 都同時走到 None 節點
            return True
                            # 不可以 else: return False 因為萬一 p.val == q.val 此時變 false
        if (not p or not q) or (p.val != q.val): #False 情況: 數值對不起來或者有一個為 None 了
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right # 正常情況的每個節點回傳