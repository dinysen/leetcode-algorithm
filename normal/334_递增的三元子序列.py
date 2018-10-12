class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        在数轴上标记两点m1,m2,满足一下代码条件
        如果数组中还有大于m2的，说明存在3元顺序子串
        """
        m1,m2 = float('inf'),float('inf');
        for i in nums:
            if i <= m1:
                m1 = i;
            elif i <= m2:
                m2 = i;
            else:
                return True;
        return False;