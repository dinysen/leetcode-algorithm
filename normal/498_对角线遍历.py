class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return [];
        i = 0;
        j = 0;
        tmp = [];
        reverseFlag = True;
        while i != len(matrix)-1 or j != len(matrix[0])-1:
            temp_i = i;
            temp_j = j;
            temp_arr = [];
            while temp_i >= 0 and temp_j < len(matrix[0]):
                temp_arr.append(matrix[temp_i][temp_j]);
                temp_i -= 1;
                temp_j += 1;
            tmp.append(temp_arr if reverseFlag else temp_arr[::-1] );
            reverseFlag = not reverseFlag;
            if i != len(matrix)-1:
                i += 1;
            else:
                j += 1;
        tmp.append([matrix[i][j]]);
        res = [];
        for i in tmp:
            res += i;
        return res;