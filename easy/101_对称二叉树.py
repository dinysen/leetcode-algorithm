# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
递归算法
def isSymmetric(self, root):

    if not root:
        return True;
    return self.isSymmetric2(root.left,root.right);

def isSymmetric2(self,tree_1,tree_2):
    if not tree_1 and not tree_2:
        return True;
    if not tree_1 or not tree_2:
        return False;
    return tree_1.val == tree_2.val and self.isSymmetric2(tree_1.left,tree_2.right) and self.isSymmetric2(tree_1.right,tree_2.left);
"""

#迭代法
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True;
        
        l = [];
        p,q = root.left,root.right;
        l.append(p);
        l.append(q);
        while len(l) != 0:
            p = l.pop();
            q = l.pop();
            
            if not p and not q:
                continue;
            if not p or not q:
                return False;
            if p.val != q.val:
                return False;
            
            l.append(p.left);
            l.append(q.right);
            
            l.append(p.right);
            l.append(q.left);
            
        return True;
    