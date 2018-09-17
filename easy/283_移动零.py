#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#必须在原数组上操作，不能拷贝额外的数组。
#尽量减少操作次数。

class Solution:
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		#这里最简单的操作就是将不是0的元素放到前面
		#当j指向0时会停止，随后i指向的整数与0互换，以此类推
		j = 0;
		for i in range(len(nums)):
			if nums[i] != 0:
			#一句执行完，与顺序执行是两回事
			nums[j],nums[i] = nums[i],nums[j];
			j+=1;
