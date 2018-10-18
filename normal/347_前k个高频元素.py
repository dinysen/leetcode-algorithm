class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s = {};
        for i in nums:
            s[i] = s[i]+1 if i in s else 1;
        s_sorted = sorted(s.items(),key = lambda x : x[1],reverse = True);
        nums_sorted = [];
        for i in s_sorted:
            nums_sorted.append(i[0]);
        return nums_sorted[:k];