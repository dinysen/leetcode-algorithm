# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
递归方式
class Solution:
    def levelOrder(self, root):
        l = [];
        return self.levelOrder2(l,0,root);
       
    def levelOrder2(self,l,level,node):
        if not node:
            return l;
        if len(l)-1<level:
            l.append([]);
        l[level].append(node.val);
        self.levelOrder2(l,level+1,node.left);
        self.levelOrder2(l,level+1,node.right);
        return l;
        
"""

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = [];
        if not root:
            return l;
        queue = [];
        queue.append(root);
        while len(queue) != 0 :
            subList = [];
            size = len(queue);
            for i in range(size):
                #此处要注意pop(0)是移出第一个值，不传参数就是移出最后一个值
                node = queue.pop(0);
                subList.append(node.val);
                if node.left:
                    queue.append(node.left);
                if node.right:
                    queue.append(node.right);
            l.append(subList);
        return l;
           