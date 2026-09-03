# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.maxDiff = 0

        def depth(root):
            if not root:
                return 0
            
            l, r = depth(root.left), depth(root.right)
            self.maxDiff = max(abs(l-r), self.maxDiff)
            print(self.maxDiff)

            return max(l, r) + 1
        

        if not root:
            return True

        l = depth(root.left)
        r = depth(root.right)

        self.maxDiff = max(abs(l-r), self.maxDiff)



        if self.maxDiff > 1:
            return False
        return True
        