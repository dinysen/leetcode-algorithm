class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        """
        天天暴力破解，一点都不优雅
        l_x , l_y = [],[];
        while x > 0:
            l_x = [x%2] + l_x;
            x = x // 2;
        while y > 0:
            l_y = [y%2] + l_y;
            y = y // 2;
        if len(l_x) != len(l_y):
            size = max(len(l_x),len(l_y));
            l_x = [0]*(size-len(l_x))+l_x;
            l_y = [0]*(size-len(l_y))+l_y;
        count = 0;
        for i in range(len(l_x)):
            if l_x[i] != l_y[i]:
                count += 1;
        return count;
        """
        l = x ^ y;
        l_str = str(bin(l));
        return l_str.count("1");
        