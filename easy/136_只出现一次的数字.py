#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#说明：
#你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

#解答：
#最好的方法是对异或操作的应用
#异或操作在python中会将10进制数字全都转为二进制来操作
#a^b=1,a^a=0,a^0=a
#a^b=b^a,a^(b^c)=(a^b)^c;
#所以在此题条件下，相同的数字两两异或操作生成0，最后只剩下个不同的数字

class Solution:
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			raise Error("非空");
		temp = 0;
		for i in nums:
			temp ^= i;
		return temp

