#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#从排序数组中删除重复项
#给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

#解答：
#利用双指针法
#慢指针对着排序后的数组
#快指针遍历当前数组
class Solution:
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) <= 1:
			return len(nums);
		i = 0;
		for j in range(1,len(nums)):
			if nums[i] == nums[j]:
				continue;
			else:
				i += 1;
				nums[i] = nums[j];
		return i+1;
