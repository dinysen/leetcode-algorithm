#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个 32 位有符号整数，将整数中的数字进行反转。

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        
        s = str(x);
        prefix,l = "",s[:];
        if "-" == s[0]:
            prefix = "-";
            l = s[1:];
        elif "0" == s[len(s)-1]:
            l = s[:len(s)-1];
        try:
            number = int(prefix+l[::-1]);
            if number > 2147483647 or number <-2147483648:
                raise ValueError("范围错误");
        except ValueError as e:
            return 0;
        return number;
        """
        x = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1]);
        return x if x <= 2147483647 and x>= -2147483648 else 0;