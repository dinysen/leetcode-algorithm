import collections;
class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [ False for i in range(len(rooms)) ];
        stack = collections.deque();
        stack.append(0);
        while len(stack) != 0:
            size = len(stack);
            if visited.count(False) == 0:
                return True;
            for i in range(size):
                roomNo = stack.popleft();
                if visited[roomNo]:
                    continue;
                visited[roomNo] = True;
                for key in rooms[roomNo]:
                    stack.append(key);
        return visited.count(False) == 0;