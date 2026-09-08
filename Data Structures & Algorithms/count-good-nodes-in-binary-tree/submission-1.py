# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0
        val = root.val
        def depth(root, val):
            if not root:
                return
            if val <= root.val:
                    self.count += 1
            val = max(root.val, val)
            depth(root.left, val)
            depth(root.right, val)
        depth(root, val)
        return self.count


        