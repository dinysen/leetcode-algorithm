import collections;
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        test = (1,1);
        stack = collections.deque();
        res =[ [ 0 for i in range(len(matrix[0]))   ] for j in range(len(matrix))] ;
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                stack.append((i,j));
                step = 0;
                visited = set();
                flag = True;
                while len(stack) != 0:
                    size = len(stack);
                    for k in range(size):
                        pos = stack.popleft();
                        if pos[0] < 0 or pos[0] >= len(matrix) or pos[1] < 0 or pos[1] >= len(matrix[0]) or pos in visited:
                            continue;
                        visited.add(pos);
                        if matrix[pos[0]][pos[1]] == 0:
                            res[i][j] = step;
                            stack.clear();
                            break;
                        else:
                            stack.append((pos[0]+1,pos[1]));
                            stack.append((pos[0]-1,pos[1]));
                            stack.append((pos[0],pos[1]+1));
                            stack.append((pos[0],pos[1]-1));
                    step += 1;
        return res;