# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfsAdd(node):
            nonlocal res 
            if not node:
                return 0
            
            left = max(0, dfsAdd(node.left))
            right = max(0, dfsAdd(node.right))

            res[0] = max(res[0], node.val+left+right)

            return node.val + max(left, right)
        
        dfsAdd(root)
        return res[0]
            