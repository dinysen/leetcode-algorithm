#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个 n × n 的二维矩阵表示一个图像。
#将图像顺时针旋转 90 度。
#说明：
#你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

#解答：
#用个map判断下就行了

class Solution:
	def rotate(self, matrix):
		"""
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        
        #先获取列数
        matrix_copy = matrix[:];
        for i in range(len(matrix_copy)):
            cl = [];
            #获取行数
            for j in range(len(matrix_copy)-1,-1,-1):
                cl.append(matrix_copy[j][i]);
            matrix[i] = cl;
        """
        
        #zip可用来进行矩阵行列互换，返回的是一个由元组组成的zip对象
        matrix[:] = map(list,zip(*matrix[::-1]));