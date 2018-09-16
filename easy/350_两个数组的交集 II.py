#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定两个数组，编写一个函数来计算它们的交集。

#解答：
#排序两个数组，每次都对两个数组中最相近的两个数字进行比较
#相同输出，不同跳过

class Solution:
	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		nums1 = sorted(nums1);
		nums2 = sorted(nums2);

		i,j = 0,0;
		l = [];
		while i <= len(nums1)-1 and j <= len(nums2)-1:
			if nums1[i] == nums2[j]:
				l.append(nums1[i]);
				i,j = i+1,j+1;
			elif nums1[i] < nums2[j]:
				i = i+1;
			elif nums1[i] > nums2[j]:
				j = j+1;
		return l;