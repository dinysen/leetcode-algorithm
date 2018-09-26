#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#报数序列是指一个整照其中的整数的顺序进数序列，按行报数，得到下一个数。其前五项如下：

#解答：
class Solution:
    
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        from functools import reduce; 
        if n == 1:
            return "1";
        
        if n == 2:
            return "11";
        
        l = "11";
        c = 3;
        while c <= n:
            total,unit = [],[];
            for i in range(len(l)-1):
                if i == 0 :
                    unit = [1,l[i]];
                if l[i] == l[i+1]:
                    unit[0] += 1;
                else :
                    total.append([str(x) for x in unit]);
                    unit = [1,l[i+1]]; 
                if i == len(l)-2:
                    total.append([str(x) for x in unit]);
            l = reduce(lambda x,y : "".join(x)+"".join(y),total);
            if isinstance(l,list):
               l = "".join(l); 
            c += 1;
        
        return l;
        