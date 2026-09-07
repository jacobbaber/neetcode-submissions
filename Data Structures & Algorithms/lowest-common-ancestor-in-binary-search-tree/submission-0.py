# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        rootQueue = [root]
        while len(rootQueue) > 0:
            nextRoot = rootQueue.pop(0)
            if p.val <= nextRoot.val and nextRoot.val <= q.val:
                return nextRoot
            if q.val <= nextRoot.val and nextRoot.val <= p.val:
                return nextRoot

            if p.val < nextRoot.val and q.val < nextRoot.val:
                rootQueue.append(nextRoot.left)
            elif p.val > nextRoot.val and q.val > nextRoot.val:
                rootQueue.append(nextRoot.right)
            else:
                rootQueue.append(nextRoot.left)
                rootQueue.append(nextRoot.right)
            
        
        