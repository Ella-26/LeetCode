# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder：
        # [root] [------左子树------] [------右子树------]
        #   0       1 ... ?               ? ... 最后
        # 找到left子树的个数就能知道怎么把list切成slide
        # inorder：
        # [------左------] [root] [------右------]
        # 0       left_size
        if not preorder:  # 空节点
            return None
        left_size = inorder.index(preorder[0])  # 左子树的大小
        left = self.buildTree(preorder[1 : 1 + left_size], inorder[:left_size])
        right = self.buildTree(preorder[1 + left_size :], inorder[1 + left_size :])
        return TreeNode(preorder[0], left, right)

