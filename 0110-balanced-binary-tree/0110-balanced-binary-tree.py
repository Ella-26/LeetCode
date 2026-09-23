# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 一次递归得到height（复用height不用重新算）+是否balance（-1表示）
    def get_height(self, node):
        if node is None:
            return 0
        left_height = self.get_height(node.left)
        if left_height == -1:  # 已经unbalanced没必要再算后面，直接传给上面-1
            return -1
        right_height = self.get_height(node.right)
        if right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.get_height(root) != -1

