class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        s = sum(nums);
        if s < S:
            return 0;
        if (S + s) % 2 != 0:
            return 0;
        
        target = int((S + s) / 2);
        dp = [0] * (target + 1);
        dp[0] = 1;
        for i in nums:
            n  = target;
            while n >= i:
                dp[n] += dp[n - i];
                n -= 1;
        return dp[target];