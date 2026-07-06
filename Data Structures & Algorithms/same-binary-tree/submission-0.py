# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stk1 = [p]
        stk2 = [q]

        while stk1 and stk2:
            node = stk1.pop()
            node2 = stk2.pop()


            if not node and not node2:
                continue
            if not node or not node2:
                return False
            if node.val != node2.val:
                return False
            
            stk1.append(node.right)
            stk1.append(node.left)
            stk2.append(node2.right)
            stk2.append(node2.left)

        return not stk1 and not stk2