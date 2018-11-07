# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections;
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [];
        stack = collections.deque();
        stack.append(root);
        res = [];
        row = 0;
        while stack:
            size = len(stack);
            tmp = [];
            row += 1;
            for i in range(size):
                node = stack.popleft();
                tmp.append(node.val);
                if node.left:
                    stack.append(node.left);
                if node.right:
                    stack.append(node.right);
            res.append(tmp[::-1] if row%2 == 0 else tmp );
        return res;
                    