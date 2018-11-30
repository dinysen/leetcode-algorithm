class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = digits[:];
        suffix = 1;
        for i in range(len(digits)-1,-1,-1):
            tmp = res[i] + suffix;
            res[i] = tmp if tmp < 10 else 0;
            if tmp < 10:
                suffix = 0;
            else:
                suffix = 1;
        if suffix == 1:
            res = [1]+res;
        return res;