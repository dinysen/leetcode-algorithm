class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s , e = 1 , x;
        while s <= e:
            mid = (s + e) // 2 ;
            if mid * mid < x:
                s = mid + 1;
            elif mid * mid > x:
                e = mid - 1;
            else:
                return mid;
        return s - 1;