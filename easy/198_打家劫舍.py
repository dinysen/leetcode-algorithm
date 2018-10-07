class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        在nums长度仅有1或2时，就返回最大值
        超过2时，就有递推公式dp[i] = max(dp[i-2]+a[i],dp[i-1]);
        """
        if len(nums) == 0:
            return 0;
        if len(nums) == 1:
            return nums[0];
        if len(nums) == 2:
            return max(nums[0],nums[1]);
        f = [nums[0],max(nums[0],nums[1])];
        for i in range(2,len(nums)):
            tmp = max(f[i-2]+nums[i],f[i-1]);
            f.append(tmp);
        return tmp;