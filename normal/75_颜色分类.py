
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        运用两次双指针
        i,j = 0,0;
        while j < len(nums):
            if nums[j] == 0:
                nums[i],nums[j] = nums[j],nums[i];
                i+=1;
            j+=1;
        j = i;
        while j<len(nums):
            if nums[j] == 1:
                nums[i],nums[j] = nums[j],nums[i];
                i+=1;
            j+=1;
        """
        l,r = 0,len(nums)-1;
        i = 0;
        while i <= r:
            if nums[i] == 0:
                nums[l],nums[i] = nums[i],nums[l];
                l+=1;
                i+=1;
            elif nums[i] == 2:
                nums[r],nums[i] = nums[i],nums[r];
                r-=1;
            else:
                i+=1;