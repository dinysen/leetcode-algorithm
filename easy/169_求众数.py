import math
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        line = math.ceil(len(nums)/2);
        m = {};
        for i in nums:
            m[i] = m[i]+1 if i in m else 1;
            if m[i] >= line:
                return i;
        return 0;
            