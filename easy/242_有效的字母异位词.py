#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #解法1
        return set(s) == set(t) and all([s.count(i) == t.count(i) for i in string.ascii_letters ])

        #解法2
        from collections import Counter
        return Counter(s) == Counter(t);