# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS: if a right exist, choose right
        # if not, choose a left

        from collections import deque
        res = []
        if not root:
            return res
        
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0: #most right element of that layer
                    res.append(node.val)

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        
        return res






