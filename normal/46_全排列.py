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

#回溯法------------------------------------------------
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = self.backtracking([],[],nums);
        return res;
        
    def backtracking(self,sub,res,nums):
        if len(nums) == 0:
            res.append(sub[:]);
        else:
            for i in range(len(nums)):
                sub.append(nums[i]);
                self.backtracking(sub,res,nums[:i]+nums[i+1:]);
                sub.pop();
        return res;