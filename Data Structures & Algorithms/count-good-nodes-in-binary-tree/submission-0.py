# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.countgoodNodes=0
        def count(node,maxValue):
            if node.val >= maxValue:
                self.countgoodNodes+=1
            if node.left:
                count(node.left,max(maxValue,node.val))
            if node.right:
                count(node.right,max(maxValue,node.val))
        count(root,root.val)
        return self.countgoodNodes
            
        