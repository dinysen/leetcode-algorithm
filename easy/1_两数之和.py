#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

#解答：
#遍历一次的方法
#将出现过值保存在dict中，后续如果出现了差值为出现过得，直接返回即可
class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""

		dic = {};
		for i in range(len(nums)):
			if target - nums[i] in dic :
				return [dic[target-nums[i]],i];
			dic[nums[i]] = i;
