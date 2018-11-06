# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
递归
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return [];
        l = [];
        l.extend(self.inorderTraversal(root.left));
        l.append(root.val);
        l.extend(self.inorderTraversal(root.right));
        return l;      
"""

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [];
        res = [];
        while True:
            if root:
                stack.append(root);
                root = root.left;
            else:
                if len(stack) == 0:
                    return res;
                node = stack.pop();
                res.append(node.val);
                root = node.right;
        return res;
