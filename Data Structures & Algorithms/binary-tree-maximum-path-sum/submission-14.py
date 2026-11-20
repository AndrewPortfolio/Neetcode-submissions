# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sumP = [root.val]

        # compute max for non split paths
        def dfsAdd(node):
            if not node:
                return 0

            left = dfsAdd(node.left)
            right = dfsAdd(node.right)
            left = max(0, left)
            right = max(0, right)

            sumP[0] = max(sumP[0], node.val + left + right)
            return node.val + max(left, right)


        dfsAdd(root)
        return sumP[0]