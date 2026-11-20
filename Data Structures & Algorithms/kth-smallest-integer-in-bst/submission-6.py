# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        visited = 0

        def dfs(node):
            nonlocal res, visited
            if not node:
                return     

            dfs(node.left)
            if visited == k:
                return 
            
            visited += 1
            if visited == k:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res