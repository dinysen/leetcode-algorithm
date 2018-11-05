class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        动态规划 还需进一步理解
        size = len(s);
        res = "";
        matrix = [[False for i in range(size)] for j in range(size) ];
        for j in range(size):
            for i in range(j+1):
                if j <= i+1 and s[i] == s[j]:
                    matrix[i][j] = True;
                    res = s[i:j+1] if len(res) < len(s[i:j+1]) else res;
                else:
                    if s[i] == s[j] and matrix[i+1][j-1]:
                        matrix[i][j] = True;
                        res = s[i:j+1] if len(res) < len(s[i:j+1]) else res;
        return res;
        """
        if len(s)==0:
            return ""
        maxlen = 1
        start = 0
        for i in range(len(s)):
            if i - maxlen >= 1 and s[i-maxlen-1:i+1]==s[i-maxlen-1:i+1][::-1]:
                start = i- maxlen -1 
                maxlen += 2
                continue
            
            if i - maxlen >= 0 and s[i-maxlen:i+1]==s[i-maxlen:i+1][::-1]:
                start = i- maxlen 
                maxlen += 1
        return s[start:start+maxlen]

-----------------------------------------------------------------
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return "";
        s = s+"&%^";
        res = "";
        size = 0;
        for i in range(len(s)):
            if len(s) - i - 1 < size:
                break;
            for j in range(len(s),i,-1):
                if s[i:j] == s[i:j][::-1] and j-i+1 > size:
                    size = j-i+1;
                    res = s[i:j];
                    break;
        return res;
-----------------------------------------------------------------------
class Solution:
    def longestPalindrome(self, s):
        size = 0;
        res = "";
        index = 0;
        for i in range(len(s)):
            if i-size-1 >= 0 and s[i-size-1:i+1] == s[i-size-1:i+1][::-1]:
                res = s[i-size-1:i+1];
                size += 2;
                continue;
            if i-size >= 0 and s[i-size:i+1] == s[i-size:i+1][::-1]:
                res = s[i-size:i+1];
                size += 1;
        return res;
                