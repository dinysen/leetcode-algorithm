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
        return self.firstBadVersion2(1,n);
        
    def firstBadVersion2(self,start,end):
        if start >= end:
            return end;
        code = (start + end)//2;
        if isBadVersion(code):
            end = code;
        else :
            start = code+1;
        return self.firstBadVersion2(start,end);

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