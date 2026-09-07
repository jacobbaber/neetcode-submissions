# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [[]]
        queue = [root]
        i = 0
        newQueue = []
        if not root:
            return []
        while len(queue) > 0:
            newRoot = queue.pop(0)
            res[i].append(newRoot.val)

            if newRoot.left:
                newQueue.append(newRoot.left)
            if newRoot.right:
                newQueue.append(newRoot.right)


            if len(queue) == 0 and len(newQueue) > 0:
                res.append([])
                queue = newQueue
                newQueue = []
                i += 1
        
        return res

            



        