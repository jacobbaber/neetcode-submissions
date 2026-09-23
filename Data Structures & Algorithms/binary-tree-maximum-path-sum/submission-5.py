# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxSum = float('-inf')
        

        def depth(root, pathSum):
            
            if not root:
                return 0        
            
            l = depth(root.left, pathSum)
            r = depth(root.right, pathSum)

            
            res = root.val
            if l > 0:
                res += l
            if r > 0:
                res += r

            self.maxSum = max(res, self.maxSum)

            return max(root.val + r, root.val + l, root.val)
        
        depth(root, 0)
        return self.maxSum
        

            




                












