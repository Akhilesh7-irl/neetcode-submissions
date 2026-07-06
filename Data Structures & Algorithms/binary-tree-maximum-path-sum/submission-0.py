# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0

            leftMx = dfs(root.left)

            rightMx = dfs(root.right)

            leftMx = max(leftMx , 0)

            rightMx = max(rightMx , 0)

            res[0] = max(res[0] , root.val+leftMx+rightMx)

            return root.val + max(leftMx , rightMx)            

        dfs(root)
        return res[0]