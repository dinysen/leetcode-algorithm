import math;
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            if 3**round(math.log(n,3)) == n:
                return True;
        return False;
        