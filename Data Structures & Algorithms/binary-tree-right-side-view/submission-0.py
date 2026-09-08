# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        highest = None
        newQ = []
        res = []

        while len(q) > 0:
            node = q.pop(0)
            if not node: continue
            highest = max(highest or 0, node.val)

            if node.left:
                newQ.append(node.left)
            if node.right:
                newQ.append(node.right)


            if len(q) == 0:
                res.append(highest)
                highest = None

                q = newQ
                newQ = []
            
        return res





        
        