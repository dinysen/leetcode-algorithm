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

#子集-回溯--------------------------------------
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.backtracking([],[],nums);
        
    def backtracking(self,res,tmp,nums):
        if sorted(tmp) in res:
            return res;
        else:
            res.append(tmp[:]);
            
        for i in range(len(nums)):
            tmp.append(nums[i]);
            self.backtracking(res,sorted(tmp),nums[:i]+nums[i+1:]);
            tmp.pop();
            
        return res;
