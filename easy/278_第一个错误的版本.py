# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

#二分查找法

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1;
        l,r,mid = 1,n,0;
        while l < r:
            mid = (l+r)//2;
            if isBadVersion(mid):
                r = mid;
            else:
                l = mid + 1;
        return l;