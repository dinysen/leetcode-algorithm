#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

#解答：
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0;
        l_n = list(needle);
        len_n = len(l_n);
        
        
        for i in range(len(haystack)-len_n+1):
            print(str(haystack[i:i+len_n]),str(needle));
            if haystack[i:i+len_n] == needle:
                return i;
        return -1;