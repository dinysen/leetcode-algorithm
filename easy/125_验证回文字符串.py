#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(" ","");
        s = s.lower();
        l = [];
        lowercase = string.ascii_lowercase+"0123456789";
        for i in s:
            if i in lowercase:
                l.append(i);
        if l == l[::-1]:
            return True;
        return False;