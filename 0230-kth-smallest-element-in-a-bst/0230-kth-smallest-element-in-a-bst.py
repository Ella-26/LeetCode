# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # 找第k小的root值，中序bst,k到0就是第k小的了
        ans = 0

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal k, ans
            if node is None or k <= 0:
                return

            dfs(node.left)

            k -= 1
            if k == 0:
                ans = node.val
            dfs(node.right)

        dfs(root)
        return ans

