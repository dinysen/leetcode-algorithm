class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #动态规划：选择最小的买入，最大的卖出
        #在计算卖出价的同时，也在选择买入价
        if len(prices) == 0:
            return 0;
        count = 0;
        minbuy = prices[0];
        for i in range(len(prices)):
            count = max(count,prices[i]-minbuy);
            minbuy = min(minbuy,prices[i]);
        return count;
        

            