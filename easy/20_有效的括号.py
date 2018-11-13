class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m_l = { '(':")", "{" : "}" , "[":"]" };
        m_r = { ")":"(", "}":"{" , "]":"[" };
        stack = [];
        if len(s) == 0:
            return True;
        for i in list(s):
            if i in m_l:
                stack.append(i);
            else:
                l = m_r[i];
                if len(stack) == 0 or stack[-1] != l:
                    return False;
                stack.pop();
        if len(stack) != 0:
            return False;
        return True;
        