class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True;
        s = str(n);
        d = {n:0};
        while True:
            n = 0;
            for i in s:
                n += int(i)*int(i);
            if n in d:
                return False;
            d[n] = 0;
            if n == 1:
                return True;
            s = str(n);
        return False;