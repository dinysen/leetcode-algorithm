#贪心算法
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True;
        reach = nums[0];
        for i in range(1,len(nums)):
            if i > reach :break;
            if i + nums[i] > reach :
                reach = i + nums[i];
        return reach >= len(nums)-1;
            