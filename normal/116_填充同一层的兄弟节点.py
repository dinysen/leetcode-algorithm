# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return;
        stack = [root];
        while len(stack) != 0:
            size = len(stack);
            for i in range(size):
                root = stack.pop(0);
                if i == size-1:
                    root.next = None;
                else:
                    root.next = stack[0];
                    
                if root.left:
                    stack.append(root.left);
                if root.right:
                    stack.append(root.right);
            