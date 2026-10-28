# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Bases cases
        if p is None and q is None:
            return True

        if not p or not q:
            return False
        
        #Check for the current nodes
        if p.val!=q.val:
            return False
        
        #Call the function recursively on both left and right tree
        leftSubTree=self.isSameTree(p.left,q.left)
        rightSubTree=self.isSameTree(p.right,q.right)

        #Combine the final results
        return leftSubTree and rightSubTree
       