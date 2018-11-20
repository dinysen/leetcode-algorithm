import string;
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = string.ascii_letters;
        nums = string.digits;
        n_stack,s_stack = [],[];
        res = "";
        num_tmp = 0;
        str_tmp = "";
        for i in s:
            if i in nums:
                num_tmp = num_tmp*10 + int(i);
            if i == "[":
                s_stack.append(str_tmp);
                n_stack.append(num_tmp);
                num_tmp = 0;
                str_tmp = "";
            if i in strs:
                str_tmp += i;
            if i == "]":
                str_tmp = n_stack.pop() * str_tmp;
                if len(n_stack) == 0:
                    res += s_stack.pop()+str_tmp;
                    str_tmp = "";
                else:
                    str_tmp = s_stack.pop() + str_tmp;
        res =  s_stack.pop()+res+str_tmp if len(s_stack) != 0 else res+str_tmp ;
        return res;
            