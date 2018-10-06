#每次只与n-2和n-1级阶梯有关

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {"n-2":1,"n-1":1};
        for i in range(1,n):
            tmp = d["n-1"];
            d["n-1"] = d["n-1"] + d["n-2"];
            d["n-2"] = tmp;
        return d["n-1"];