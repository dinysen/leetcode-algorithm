class Solution(object):
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
        l = [[1],[1,1]];
        n = 2;
        while n < numRows:
            t_l = [1] + [l[-1][i]+l[-1][i+1] for i in range(len(l[-1])-1)] + [1];
            l.append(t_l);
            n += 1;
        return l;