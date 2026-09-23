# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:  # 已经过了上面那个说明一定有一个not none，所以不同
            return False
        # 到这里说明都有值，看root的left和root的right和是否same
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.right)
            and self.isSameTree(p.right, q.left)
        )

    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.isSameTree(root.left, root.right)

