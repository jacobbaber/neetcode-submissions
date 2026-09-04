# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.same = True

        def depth(p, q):
            if not p and not q:
                return None
            
            if not p or not q:
                self.same = False
                return None
            

            elif p.val != q.val:
                self.same = False
                return None

            depth(p.left, q.left)
            depth(p.right, q.right)

        depth(p,q)

        return self.same
            


            
        