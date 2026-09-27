# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.s = ""


        def dfs(root):
            if not root:
                self.s += " #"
                return
            self.s += f" {root.val}"
            l = dfs(root.left)
            r = dfs(root.right)
        
        dfs(root)
        print(self.s)
        return self.s




            


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        s = data.split(" ")[1:len(data)]

        self.curr = 0

        def dfs():
            val = s[self.curr]
            self.curr += 1
            if val == "#":
                return
            
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()

            return node
    
 
        return dfs()

      