# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root

        if not root or not p or not q:
            return None
        
        

        if p.val < node.val and q.val < node.val:
            return self.lowestCommonAncestor(node.left , p ,q)

        if p.val > node.val and q.val > node.val:
            return self.lowestCommonAncestor(node.right , p ,q)

        else:
            return node
        

        
        