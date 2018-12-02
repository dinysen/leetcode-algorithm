class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return [];
        visited = set([]);
        res = [];
        row = len(matrix);
        col = len(matrix[0]);
        i,j = 0,0;
        while len(visited) < row*col:
            res.append(matrix[i][j]);
            visited.add((i,j));
            rightFlag = False;
            downFlag = False;
            leftFlag = False;
            if j < col-1 and (i,j+1) not in visited:
                j += 1;
                rightFlag = True;
            elif i < row-1 and (i+1,j) not in visited:
                i += 1;
                downFlag = True;
            elif j > 0 and (i,j-1) not in visited:
                j -= 1;
                leftFlag = True;
            if i > 0 and not downFlag and not leftFlag and (i-1,j) not in visited:
                if rightFlag:
                    j -= 1;
                i -= 1;
        return res;