class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]];
        for i in nums:
            res = res + [[i] + l for l in res ];
        return res;