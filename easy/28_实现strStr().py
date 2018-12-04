class Solution:
    
    def getNext(self,needle):
        res = [0 for i in range(len(needle))];
        res[0] = -1;
        k = -1;
        j = 0;
        while j < len(needle)-1:
            if k == -1 or needle[k] == needle[j]:
                k += 1;
                j += 1;
                res[j] = k;
            else:
                k = res[k];
        return res;
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0 :
            return 0;
        next_arr = self.getNext(needle);
        i,j = 0,0;
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == len(needle)-1:
                    return i - len(needle) + 1;
                i += 1;
                j += 1;
            else:
                j = next_arr[j];
                if j == -1:
                    i += 1;
                    j = 0;
        return -1;
                