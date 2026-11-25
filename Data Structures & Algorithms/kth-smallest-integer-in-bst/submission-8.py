# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = 0
        res = root.val
        def dfsFindMin(node):
            nonlocal visited, res
            if not node:
                return 
            
            dfsFindMin(node.left)
            if visited == k:
                return 

            visited += 1
            if visited == k:
                res = node.val
                return
            dfsFindMin(node.right)
            
        
        dfsFindMin(root)
        return res