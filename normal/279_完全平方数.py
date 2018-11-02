import collections;
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = collections.deque();
        stack.append(n);
        visited = set([n]);
        count = 0;
        while stack:
            size = len(stack);
            count += 1;
            for i in range(size):
                number = stack.popleft();
                for j in range(1,n+1):
                    t_number = number - (j ** 2);
                    if t_number == 0:
                        return count;
                    if t_number in visited:
                        continue;
                    if t_number < 0:
                        break;
                    stack.append(t_number);
                    visited.add(t_number);
        return -1;