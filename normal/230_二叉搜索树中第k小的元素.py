# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#暴力破解
import collections;
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = sorted(self.preOrder(root,[]));
        return l[k-1];
        
    
    def preOrder(self,root,l):
        if not root:
            return l;
        l.append(root.val);
        l = self.preOrder(root.left,l);
        l = self.preOrder(root.right,l);
        return l;

-------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections;
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [];
        while True:
            if root:
                stack.append(root);
                root = root.left;
            else:
                node = stack.pop();
                k -= 1;
                if k == 0:
                    return node.val;
                else:
                    root = node.right;