import collections;
class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1;
        deadends = set(deadends)
        stack = collections.deque();
        stack.append("0000");
        visited = set(["0000"]);
        count = 0;
        while len(stack) != 0:
            size = len(stack);
            count += 1;
            for i in range(size):
                point = stack.popleft();
                for j in range(4):
                    for k in range(-1,2,2):
                        newPoint = [i for i in point]
                        newPoint[j] = chr((ord(newPoint[j]) - ord('0') + k + 10) % 10 + ord('0'))
                        newPoint = "".join(newPoint)
                        
                        if newPoint in visited or newPoint in(deadends):
                            continue;
                        if newPoint == target:
                            return count;
                        visited.add(newPoint);
                        stack.append(newPoint);
                        
            
        return -1;