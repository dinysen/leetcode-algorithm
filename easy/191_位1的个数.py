class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 :
            return 0;
        count = 1;
        while n > 2:
            if n % 2 ==1 :
                count += 1;
            n = n / 2;
        return count;
        