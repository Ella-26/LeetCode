# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 转换每个节点的左右子树
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None
        root.left, root.right = root.right, root.left  # 交换
        self.invertTree(root.left)  # 递归处理（原右子树）
        self.invertTree(root.right)  # 递归处理（原左子树）
        return root

