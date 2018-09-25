#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        dict_s = {};
        for i in s:
            if i in dict_s:
                dict_s[i] = dict_s[i]+1;
            else:
                dict_s[i] = 1;
        
        dict_t = {};
        for j in t:
            if j in dict_t:
                dict_t[j] = dict_t[j]+1;
            else:
                dict_t[j] = 1;
        
        if len(dict_s) != len(dict_t):
            return False;
                
        print(str(dict_s),str(dict_t));
        for key,val in dict_s.items():
            if val != dict_t.get(key,0):
                return False;
        return True
        """
        return set(s) == set(t) and all([s.count(i) == t.count(i) for i in string.ascii_letters ])