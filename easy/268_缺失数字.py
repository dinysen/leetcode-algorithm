class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        运用异或的方法
        res = 0;
        nums.append(0);
        for i in range(len(nums)):
            res ^= nums[i] ^ i;
        return res;
        """
        #和法
        num_sum = (1+len(nums))*len(nums)*0.5;
        return int(num_sum - sum(nums));
        