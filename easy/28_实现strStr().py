class Solution:
    
    def getNext(self,needle):
        self.next = [ 0 for i in range(len(needle)) ];
        self.next[0] = -1;
        n_l = list(needle);
        k = -1;
        j = 0;
        while j < len(needle)-1:
            if k == -1 or n_l[k] == n_l[j]:
                k += 1;
                j += 1;
                self.next[j] = k;
            else:
                k = self.next[k];
                
            
    
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