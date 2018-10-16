class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = [];
        self.generateParentthesisIter("",n,n);
        return self.res;
        
    def generateParentthesisIter(self,content,l,r):
        if l == 0 and r == 0:
            self.res.append(content);
        if l > 0:
            self.generateParentthesisIter(content+"(",l-1,r);
        if r > l:
            self.generateParentthesisIter(content+")",l,r-1);
            