# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       
        self.isCopy = False
        def depth(r):
            if self.isCopy == True:
                return
            if not r: return

            if r.val == subRoot.val:
                self.isCopy = compare(r, subRoot)

            depth(r.left)
            depth(r.right)
        
        def compare(p, q):
            if not p and not q:
                return True
            if not q and p:
                return False
            if not p and q:
                return False
            if p.val != q.val:
                return False

            print(p.val)
            
            l = compare(p.left, q.left)
            r = compare(p.right, q.right)
            
            print(l)
            print(r)
            return (l and r)

        depth(root)
        return self.isCopy

            


        
            
            

            


        