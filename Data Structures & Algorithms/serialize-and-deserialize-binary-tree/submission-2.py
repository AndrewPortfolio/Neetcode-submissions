# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialize = []

        def dfsString(node):
            if not node:
                serialize.append("N")
                return 
            
            serialize.append(str(node.val))

            left = dfsString(node.left)
            if left: serialize.append(str(left.val))

            right = dfsString(node.right)
            if right: serialize.append(str(right.val))

            return 

        dfsString(root) 
        return ",".join(serialize)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfsCreateTree():
            if vals[self.i] == 'N':
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfsCreateTree()
            node.right = dfsCreateTree()

            return node
        
        return dfsCreateTree()

