class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxIndex = 0;
        for i in range(len(nums)):
            if nums[i] > nums[maxIndex]:
                maxIndex = i;
        
        maxNumber = nums[maxIndex];
        nums[maxIndex] = 0;
        secondMax = max(nums);
        if maxNumber >= secondMax * 2:
            return maxIndex;
        else:
            return -1;