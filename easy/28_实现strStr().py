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
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i;
        return -1;

#KMP next方法应该还能优化
class Solution:
    
    def getNext(self,needle):
        self.next = [-1];
        for i in range(1,len(needle)):
            sub = needle[:i];
            l = len(sub)-1;
            while l > 0 and sub[:l] != sub[len(sub)-l:len(sub)]:
                l -= 1;
            self.next.append(l);
                
            
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0;
        self.getNext(needle);
        i,j = 0,0;
        while i < len(haystack):
            print(i,j,haystack[i] == needle[j]);
            if haystack[i] == needle[j]:
                if j == len(needle)-1:
                    return i - len(needle) + 1;
                i+=1;
                j+=1;
            else:
                j = self.next[j];
                if j == -1:
                    i +=1;
                    j = 0;
        return -1;