# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        from collections import deque
        if not root:
            return 0

        q = deque([root])
        level = 0

        while q: # until queue 沒東西才結束

            for i in range(len(q)): # 加這層的 node 的 subtree 進 queue
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1 #跑了幾圈就是做了幾層

        return level

        
        
        """
        BFS 骨幹：
        
        q = deque([start])
        while q:
            for i in range(len(q)):
                # popleft
                # append

        """

