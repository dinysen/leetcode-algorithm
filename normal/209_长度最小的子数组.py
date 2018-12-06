class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,-1;
        length = len(nums)+1;
        total = 0;
        while l < len(nums):
            if r<len(nums)-1 and total < s:
                r+=1;
                total += nums[r];
            else:
                total -= nums[l];
                l += 1;
            if total >= s:
                length = min(length,r-l+1);
        if length == len(nums)+1:
            return 0;
        return length;
                