# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.curr = 0
        inorderIdx = {}
        for i in range(len(inorder)):
            inorderIdx[inorder[i]] = i


        def depth(l, r):
            if l > r:
                return None

            rootVal = preorder[self.curr]
            self.curr += 1
            root = TreeNode(rootVal)
            mid = inorderIdx[rootVal]
            root.left = depth(l, mid - 1)
            root.right = depth(mid + 1, r)

            return root
        

        return depth(0, len(inorder) - 1)

        