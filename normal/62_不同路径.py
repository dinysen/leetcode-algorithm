class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1 or n <= 1:
            return 1;
        
        d = [ [ 1 if i==0 or j==0 else 0 for i in range(m) ] for j in range(n) ];
        for i in range(1,n):
            for j in range(1,m):
                d[i][j] = d[i-1][j] + d[i][j-1];
                
        return d[n-1][m-1];