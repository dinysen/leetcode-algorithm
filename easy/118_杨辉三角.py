class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [];
        if numRows == 1:
            return [[1]];
        if numRows == 2:
            return [[1],[1,1]];
        res = [[1],[1,1]];
        for i in range(1,numRows-1):
            tmp = [1] + [ res[i][j]+res[i][j+1] for j in range(len(res[i])-1) ] + [1];
            res.append(tmp);
        return res;