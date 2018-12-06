class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0;
        i,j = 0,0;
        while i < len(nums):
            if nums[i]==1 and nums[j]==1:
                i+=1;
            elif nums[i]==0 and nums[j]==1:
                length = i-j if i-j > length else length;
                j = i+1;
                i+=1;
            elif nums[i] == 0 and nums[j] == 0:
                i+=1;
                j+=1;
        length = i-j if i-j > length else length;
        return length;
        