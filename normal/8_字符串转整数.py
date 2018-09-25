#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#实现 atoi，将字符串转为整数。

#解答：
#通过正则表达式获取元素
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        result = re.findall(r"^[\+\-]?\d+",str.strip());
        if result != []:
            if int(result[0]) < -(2 ** 31):
                return -(2 ** 31);
            elif int(result[0]) > 2**31-1:
                return 2**31-1;
            else:
                return int(result[0]);
        else:
            return 0;