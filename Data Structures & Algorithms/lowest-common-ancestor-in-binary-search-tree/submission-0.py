# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p and q are in different sides of the tree the lca is the root
        #check if both p and q are either greater or less than the current root'
        #if less than: recursion on the left
        #elif greater:recursion on the right
        print(root.val)
        if not root:
            return None
        if root==p or root==q:
            return root
        if (p.val<root.val and q.val>root.val) or (p.val>root.val and q.val<root.val):
            return root
        elif p.val < root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
        
