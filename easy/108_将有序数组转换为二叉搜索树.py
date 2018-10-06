# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    二分查找法
    根节点为数组的中间节点，然后数组被分为左右两段
    左子树的节点就是左边数组的中间节点
    右子树的节点就是右边数组的中间节点，以此类推
    """
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBST2(nums,0,len(nums)-1);
        
    def sortedArrayToBST2(self,nums,left,right):
        if left>right :
            return None;
        mid = (left + right)//2;
        node = TreeNode(nums[mid]);
        node.left = self.sortedArrayToBST2(nums,left,mid-1);
        node.right = self.sortedArrayToBST2(nums,mid+1,right);
        return node;