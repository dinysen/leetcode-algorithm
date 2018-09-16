#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个整数数组，判断是否存在重复元素。
#如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

#解答：
#用个map判断下就行了

class Solution:
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		d = {};
		for i in nums:
			if i in d:
				return True;
			else:
				d[i] = i;
		return False;
