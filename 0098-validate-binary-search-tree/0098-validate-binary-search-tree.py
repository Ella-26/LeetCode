# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None, left=-inf, right=inf) -> bool:
        if root == None:
            return True
        x = root.val
        return (
            left < x < right
            and self.isValidBST(root.left, left, x)
            and self.isValidBST(root.right, x, right)
        )

