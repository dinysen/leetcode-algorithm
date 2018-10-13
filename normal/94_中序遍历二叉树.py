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
        stack = [];
        result = [];
        while len(stack) != 0 or root:
            if root:
                stack.append(root);
                root = root.left;
            else:
                root = stack.pop();
                result.append(root.val);
                root = root.right;
        return result;
