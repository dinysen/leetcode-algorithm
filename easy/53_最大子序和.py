class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        动态规划：核心就是找到一个递推公式
        D[i] = max(D[i-1]+a[i],a[i]);
        count = -float('inf');
        this_sum = 0;
        for i in nums:
            this_sum = max(this_sum+i,i);
            count = max(count,this_sum);
        return count;
        """
        """
        还有种分治法，以后再议
        """