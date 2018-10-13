# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归方式
"""
class Solution:
    def inorderTraversal(self, root):
        l = [];
        l = self.inorderTraversal2(root,l);
        return l;
        
    def inorderTraversal2(self,root,l):
        if not root:
            return l;
        self.inorderTraversal2(root.left,l);
        l.append(root.val);
        self.inorderTraversal2(root.right,l);
        return l;
"""

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [];
        result = [];
        while len(stack) > 0 or root:
            if root:
                stack.append(root);
                root = root.left;
            else:
                root = stack.pop();
                result.append(root.val);
                root = root.right;
        return result;