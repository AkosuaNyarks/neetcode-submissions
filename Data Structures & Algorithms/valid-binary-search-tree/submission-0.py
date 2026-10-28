# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(node,minAllowed,maxAllowed):
            if not node:
                return True
            if not (minAllowed<node.val  and maxAllowed > node.val ):
                return False
            return bst(node.left,minAllowed,node.val) and bst(node.right,node.val,maxAllowed)
        return bst(root, float("-inf"),float("inf"))

        