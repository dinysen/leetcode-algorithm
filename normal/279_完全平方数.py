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

#动态规划算法，LTE，就当做思路的一种吧
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]+[0xffffffff]*(n);
        dp[1] = 1;
        for i in range(2,n+1):
            j = 1;
            while j*j <= n:
                dp[i] = min(dp[i],(dp[i-j*j])+1);
                j += 1;
        return dp[-1];