#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
"""
        :type s: str
        :rtype: bool
        """
        """
        s_copy = "";
        for i in s:
            if i in string.ascii_letters+string.digits :
                s_copy += i.lower();
        return s_copy == s_copy[::-1];
        """
        """
        s_copy = "".join(list(filter(str.isalnum,s))).lower();
        return s_copy == s_copy[::-1];
        """
        import re
        s_copy = re.sub(r'[^a-z|0-9]+','',s.lower());
        return s_copy == s_copy[::-1];
