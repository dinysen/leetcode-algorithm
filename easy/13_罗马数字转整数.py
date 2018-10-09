class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        
        """
        count = 0;
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000};
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                count -= d[s[i]];
            else:
                count += d[s[i]];
        return count + d[s[-1]];