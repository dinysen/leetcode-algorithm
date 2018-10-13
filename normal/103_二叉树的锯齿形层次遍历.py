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
        stack = [root];
        line = 1;
        result = [];
        while len(stack) != 0:
            subList = [];
            size = len(stack);
            for i in range(size):
                node = stack.pop(0);
                subList.append(node.val);
                if node.left:
                    stack.append(node.left);
                if node.right:
                    stack.append(node.right);
                
            
            result.append(subList if line % 2 ==1 else subList[::-1] );
            line += 1;
        
        return result;