# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#解题思路
#找到前序中的第一个节点（根节点）在中序中的位置，此位置左边全是左子树，右边全是右子树
#随后左子树数组的长度对应着前序中左子树的长度，右子树亦然
#随后进行递归
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 :
            return None;
        root = TreeNode(preorder[0]);
        index = inorder.index(root.val);
        root.left = self.buildTree(preorder[1:index+1],inorder[:index]);
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:]);
        return root;