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