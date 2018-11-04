from functools import reduce;
class Solution:
    """
    找一个基准点，然后转化为双指针法来计算两数之和
    """
    def threeSum(self, nums):

        nums = sorted(nums);
        l = [];
        s = set();
        for i in range(len(nums)):
            if i != 0 and nums[i-1] == nums[i]:
                continue;
            if nums[i] > 0:
                break;
            k = nums[i];
            target = 0 - k;
            j,k = i+1,len(nums)-1;
            while j < k:
                if nums[j] + nums[k] == target and not (str(nums[i])+str(nums[j])+str(nums[k])) in s:
                    l.append([nums[i],nums[j],nums[k]]);
                    s.add(str(nums[i])+str(nums[j])+str(nums[k]));
                    while j < k and nums[j] == nums[j+1]:
                        j+=1;
                    while j < k and nums[k] == nums[k-1]:
                        k-=1;
                    j += 1;k -= 1;
                elif nums[j] + nums[k] > target:
                    k -= 1;
                else:
                    j += 1;
        return l;

#暴力破解，LTE
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums);
        res = [];
        visited = set();
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break;
            for j in range(i+1,len(nums)-1):
                if nums[i] + nums[j] > 0:
                    continue;
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and str(nums[i])+str(nums[j])+str(nums[k]) not in visited:
                        res.append([nums[i],nums[j],nums[k]]);
                        visited.add(str(nums[i])+str(nums[j])+str(nums[k]));
        return res;