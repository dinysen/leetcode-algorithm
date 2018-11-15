# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

import collections;
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None;
        stack = collections.deque();
        stack.append(node);
        m = {};
        visited = set([]);
        while len(stack) != 0 :
            node_cur = stack.popleft();
            if node_cur in visited:
                continue;
            visited.add(node_cur);
            node_copy = m.get(node_cur,UndirectedGraphNode(node_cur.label));
            for i in node_cur.neighbors:
                stack.append(i);
                neighbor = m.get(i,UndirectedGraphNode(i.label));
                m[i] = neighbor;
                node_copy.neighbors.append(neighbor);
            m[node_cur] = node_copy;
        return m[node]
        