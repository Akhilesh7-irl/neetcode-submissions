# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(curr,maxval):
            if not curr:
                return 0
            
            good = 1 if curr.val >= maxval else 0

            maxval = max(maxval,curr.val)

            lftgood = dfs(curr.left , maxval)
            rghtgood = dfs(curr.right, maxval)

            
            return good+lftgood+rghtgood

        return dfs(root , root.val)

        

            

                