# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        if not root:
            return res
        

        def dfs(curr , maxval):
            
            nonlocal res
            
            if not curr:
                return


            maxval = max(curr.val , maxval)

            if curr.val >= maxval:
                res += 1

            dfs(curr.left , maxval)
            dfs(curr.right , maxval)        


        dfs(root , root.val)

        return res

            

                