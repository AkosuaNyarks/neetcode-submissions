# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum=float("-inf")
        def PathSum(root):
            if not root:
                return 0
            left=max(0,PathSum(root.left))
            right=max(0,PathSum(root.right))
            self.maxPathSum=max(self.maxPathSum,left+right+root.val)
            return max(left,right)+root.val
        PathSum(root)
        return self.maxPathSum
