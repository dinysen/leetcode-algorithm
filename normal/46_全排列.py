class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums];
        res = [];
        for i,num in enumerate(nums):
            next_num = nums[:i]+nums[i+1:];
            for j in self.permute(next_num):
                res.append([num]+j);
        return res;