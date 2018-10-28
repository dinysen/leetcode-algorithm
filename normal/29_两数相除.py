class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #小于0就是负号
        symbol = (dividend ^ divisor) < 0;
        dividend = abs(dividend);
        divisor = abs(divisor);
        quotient = 0;
        for i in range(31,-1,-1):
            if (dividend >> i) >= divisor:
                quotient += 1 << i;
                dividend -= divisor << i;
                
        quotient = -quotient if symbol else quotient
                
        if quotient < -2**31 or quotient > (2**31) -1:
            return 2**31 -1
        return quotient;
        