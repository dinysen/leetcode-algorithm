#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

#解答：
#此题的重点就是找到分界线
#分界线的前半部分直接移动到数组的后半段
#分界线的后半部分，直接移动到数组的前半段即可
class Solution:
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		nums_len = len(nums);
		nums[:] = nums[(nums_len - k):] + nums[:nums_len-k];
