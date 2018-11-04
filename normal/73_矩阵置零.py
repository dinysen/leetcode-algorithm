class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """
        O(m*n)
        x,y = set(),set();
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x.add(j);
                    y.add(i);
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in y or j in x:
                    matrix[i][j] = 0 ;
        """
        f_row = f_col = False;
        for i in matrix[0]:
            if i == 0:
                f_row = True;
                
        for i in matrix:
            if i[0] == 0:
                f_col = True;
                
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
            
        for i in range(1,len(matrix[0])):
            if matrix[0][i] == 0:
                for x in range(len(matrix)):
                    matrix[x][i] = 0;
                    
        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0]*len(matrix[0]);
                
        if f_row:
            matrix[0] = [0]*len(matrix[0]);
            
        if f_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0;

-----------------------------------------------------------------------
        
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return None;
        
        t = [];
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    t.append((i,j));
        
        while t:
            (i,j) = t.pop();
            matrix[i] = [0] * len(matrix[0]);
            for item in matrix:
                item[j] = 0;
        
        
            