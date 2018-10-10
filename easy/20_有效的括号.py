class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        '('，')'，'{'，'}'，'['，']'
        """
        d_r = {"(":")","{":"}","[":"]"};
        d_l = {")":"(","}":"{","]":"["};
        l = [];
        for i in s:
            if i in d_r:
                l.append(i);
            if i in d_l:
                if len(l) == 0 or d_l[i] != l[-1]:
                    return False;
                l.pop();
        if len(l) != 0:
            return False;
        return True;
        