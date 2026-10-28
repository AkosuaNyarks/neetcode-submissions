# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        #make a queue
        queue=[root]
        while queue:
            #pop the first element in the queue
            current=queue.pop(0)
            #save the left node in a variable temp
            temp=current.left
            #swap the left node with the right node
            current.left=current.right
            #swap the right node with the left node
            current.right=temp
            # if the left child exists, enqueue
            if current.left is not None:
                queue.append(current.left)
            # if the right child exists, enqueue
            if current.right is not None:
                queue.append(current.right)
        return root

        