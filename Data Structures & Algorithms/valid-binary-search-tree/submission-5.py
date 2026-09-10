# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        def depth(root, minVal, maxVal):
            if not root:
                return True

            
            
            if root.val <= minVal or root.val >= maxVal:
                return False

            
            
            l = depth(root.left, minVal, root.val)
            r = depth(root.right, root.val, maxVal)

            return (l and r)
            

        return depth(root, float("-inf"), float("inf"))