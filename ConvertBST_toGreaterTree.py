# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumOfValues = 0

        def traverse(node):

            if not node:
                return
            nonlocal sumOfValues
            
            if node.right is not None:
                traverse(node.right)
            #update
            temp = node.val
            node.val += sumOfValues
            sumOfValues += temp 
            if node.left is not None:
                traverse(node.left)

        traverse(root)
        return root

