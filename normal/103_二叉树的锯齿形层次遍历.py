# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [];
        l = [];
        stack = [root];
        i = 1;
        while len(stack) != 0:
            size = len(stack);
            subList = [];
            stack_inuse = stack[::-1] if i%2 == 0 else stack[:];
            for index in range(size):
                node_inval = stack_inuse.pop(0);
                node = stack.pop(0);
                subList.append(node_inval.val);
                if node.left:
                    stack.append(node.left);
                if node.right:
                    stack.append(node.right);
            i += 1;
            l.append(subList);
        return l;