#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#从排序数组中删除重复项
#编写一个函数来查找字符串数组中的最长公共前缀。

#如果不存在公共前缀，返回空字符串 ""。

#解答：
#先找出数组中长度最短的一项，遍历此项
class Solution:
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return "";
        from functools import reduce
        shortest_str = reduce(lambda x,y : x if len(x) < len(y) else y,strs);
        if len(shortest_str) == 0:
            return "";
        for index,val in enumerate(shortest_str):
            for j in strs:
                if shortest_str[:index+1] != j[:index+1]:
                    return "" if index == 0 else shortest_str[:index];
        return shortest_str[:index+1];
