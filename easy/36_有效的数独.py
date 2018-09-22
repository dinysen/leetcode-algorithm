#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

#数字 1-9 在每一行只能出现一次。
#数字 1-9 在每一列只能出现一次。
#数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

#解答：
#用空间换取时间，遍历一次将行、列与每个小块中的数字情况都保留下来
class Solution:

	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		
		ROW = [[] for i in range(9)];
		CELL = [[] for i in range(9)];
		BLOCK = [[] for i in range(9)];
		for i,row in enumerate(board):
			for j,cell in enumerate(row):
				k = (i//3)*3+(j//3);
				if row[j] != ".":
					if row[j] in ROW[i]+CELL[j]+BLOCK[k]:
						return False;
					ROW[i].append(row[j]);
					CELL[j].append(row[j]);
					BLOCK[k].append(row[j]);
		return True;