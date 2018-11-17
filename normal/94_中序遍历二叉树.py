# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return [];
        stack = [];
        res = [];
        cur = root;
        while len(stack) != 0 or cur:
            while cur:
                stack.append(cur);
                cur = cur.left;
            cur = stack.pop();
            res.append(cur.val);
            cur = cur.right;
        return res;