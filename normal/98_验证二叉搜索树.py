# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBST2(root,-float('inf'),float('inf'));
        
    def isValidBST2(self,root,small,large):
        if not root:
            return True;
        if root.val >= large or root.val <= small:
            return False;
        return self.isValidBST2(root.left,small,root.val) and self.isValidBST2(root.right,root.val,large);