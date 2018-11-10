#回溯法，其实就是穷举法
#一般运用递归的方式实现
#递归函数中需要传递还未完成的解与边界条件
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = self.dfs("",[],n,n);
        return res;
        
    def dfs(self,sub,res,lnum,rnum):
        if lnum == 0 and rnum == 0:
            res.append(sub);
        if rnum > lnum:
            self.dfs(sub+")",res,lnum,rnum-1);
        if lnum > 0:
            self.dfs(sub+"(",res,lnum-1,rnum);
        return res;