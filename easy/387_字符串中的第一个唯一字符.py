#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        
        s_copy = list(s[:]);
        dic = {};
        for i,val in enumerate(s):
            if val in dic:
                s_copy[i] = "0";
                s_copy[dic[val]] = "0";
            else:
                dic[val] = i;
        if len(s_copy) == 0:
            return -1;
        for i,val in enumerate(s_copy):
            if val != "0":
                return i;
            if i == len(s_copy)-1:
                return -1;
        """
        # s.count()直接可以统计字符个数，s.index()可以找出特定字符的位置，，，，这道题就没什么难度了
        str_lowercase = string.ascii_lowercase;
        s = [s.index(label) for label in str_lowercase if s.count(label) == 1];
        return min(s) if len(s) > 0 else -1;