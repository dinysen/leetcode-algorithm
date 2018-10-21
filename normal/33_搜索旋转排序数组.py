class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        rever_index = 0;
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                rever_index = i+1;
                break;
        
        nums_1,nums_2 = nums[:rever_index],nums[rever_index:];
        l_1,r_1 = 0,len(nums_1)-1;
        while l_1 <= r_1:
            k = (l_1+r_1) // 2;
            if nums_1[k] == target:
                return k;
            elif nums_1[k] > target:
                r_1 = k-1;
            else:
                l_1 = k+1;
            
        l_2,r_2 = 0,len(nums_2)-1;
        while l_2 <= r_2:
            k = (l_2+r_2) // 2;
            if nums_2[k] == target:
                return k+len(nums_1);
            elif nums_2[k] > target:
                r_2 = k-1;
            else:
                l_2 = k+1;
        
        return -1;
            