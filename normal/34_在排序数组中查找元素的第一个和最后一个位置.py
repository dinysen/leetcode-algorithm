"""
运用一次二分法找到目标值，然后以目标值为中心扩散，这种方法超时了
class Solution:
    def searchRange(self, nums, target):
        l,r = 0,len(nums)-1;
        res = [-1,-1];
        while l <= r:
            mid = (l+r)//2;
            if nums[mid] == target:
                while mid >= l and nums[mid] == target:
                    mid -= 1;
                mid += 1;
                res[0] = mid;
                while mid <= r and nums[mid] == target:
                    mid += 1;
                mid -= 1;
                res[1] = mid;
                return res;
            elif nums[mid] < target:
                l = mid;
            else:
                r = mid;
        return res;
"""

"""
运用两次二分法，分别查找起始点与终止点
"""
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1];
        res[0] = self.findFirst(nums,target);
        res[1] = self.findLast(nums,target);
        return res;

    def findFirst(self,nums,target):
        l,r = 0,len(nums)-1;
        index = -1;
        while l <= r:
            m = (l+r) //2;
            if nums[m] >= target:
                r = m -1;
            else:
                l = m + 1;
            if nums[m] == target:
                index = m;
        return index;
    
    def findLast(self,nums,target):
        l,r = 0,len(nums)-1;
        index = -1;
        while l <= r:
            m = (l+r) // 2;
            if nums[m] <= target:
                l = m + 1;
            else:
                r = m - 1;
            if nums[m] == target:
                index = m;
        return index;
        