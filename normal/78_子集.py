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

#子集-回溯 LTE--------------------------------------
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = [];
        self.backtracking([],nums);
        return self.res;
        
    def backtracking(self,sub,nums):
        if sub not in self.res:
            self.res.append(sub[:]);
        for i in range(len(nums)):
            sub.append(nums[i]);
            self.backtracking(sorted(sub),nums[:i]+nums[i+1:]);
            sub.pop();
