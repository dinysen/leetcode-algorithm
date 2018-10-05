# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#后序遍历算法
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0;
        if root:
            ldepth = self.maxDepth(root.left);
            rdepth = self.maxDepth(root.right);
            depth = ldepth + 1 if ldepth > rdepth else rdepth + 1;
        return depth;
            