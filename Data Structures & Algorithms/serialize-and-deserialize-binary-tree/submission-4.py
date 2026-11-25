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

        def dfsString(node: Optional[TreeNode]):
            if not node:
                serialize.append('N')
                return 
            
            serialize.append(str(node.val))
            dfsString(node.left)
            dfsString(node.right)


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
            
            newNode = TreeNode(vals[self.i])
            self.i += 1
            newNode.left = dfsCreateTree()
            newNode.right = dfsCreateTree()

            return newNode

        
        return dfsCreateTree()