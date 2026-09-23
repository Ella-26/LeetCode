# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # 先遍历右子树，深度=答案长度就加进答案，再遍历左子树（只有左比右深才可能看到）
        ans = []

        def f(node, depth):
            if node is None:
                return
            if depth == len(ans):
                ans.append(node.val)
            f(node.right, depth + 1)
            f(node.left, depth + 1)

        f(root, 0)
        return ans

