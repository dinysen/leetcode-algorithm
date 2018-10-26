class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0;
        while n > 0:
            c += n //5;
            n //= 5;
        return c;