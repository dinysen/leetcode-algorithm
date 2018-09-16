#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#你可以假设除了整数 0 之外，这个整数不会以零开头。

#解答：
#遇到这种从数组末尾做运算的，我一般都是把数组倒着做

class Solution:
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		n = 0;
		l = digits[::-1];
		new_l = [];
		for i,val in enumerate(l):
			if i == 0 or n == 1 :
				val += 1;
				n = 0;
			if val == 10:
				new_l.append(0);
				n = 1;
			else:
				new_l.append(val);
			if i == len(l)-1 and n == 1:
				new_l.append(1);
		return new_l[::-1];