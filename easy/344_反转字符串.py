class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i,j = 0,len(s)-1;
        list_s = list(s);
        while i < j:
            list_s[i],list_s[j] = list_s[j],list_s[i];
            i+=1;
            j-=1;
        return "".join(list_s);