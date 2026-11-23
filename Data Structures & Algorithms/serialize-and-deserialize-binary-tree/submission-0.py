# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        encoded = []
        def dfsAdd(node):
            nonlocal encoded
            if not node:
                encoded.append("N")
                return
            
            encoded.append(str(node.val))
            dfsAdd(node.left)
            dfsAdd(node.right)

        
        dfsAdd(root)
        return ",".join(encoded)

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or len(data) == 0:
            return None
        
        decoded = data.split(",")
        self.i = 0

        def dfsAddChild():
            if decoded[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(decoded[self.i])
            node.left = dfsAddChild()
            node.right = dfsAddChild()

        return root

