class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1;
        if len(nums) == 0:
            return res;
        count_l = 0;
        count_r = sum(nums) - nums[0];
        if count_l == count_r:
            return 0;
        for i in range(1,len(nums)):
            count_l += nums[i-1];
            count_r -= nums[i];
            if count_l == count_r:
                return i;
        return res;