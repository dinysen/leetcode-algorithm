class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = "";
        l = 0;
        for ch in s:
            if not ch in res:
                res += ch;
            else:
                l = max(len(res),l);
                index = res.index(ch);
                res = res[index+1:]+ch;
            l = max(len(res),l);
        return l;