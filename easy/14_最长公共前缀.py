from functools import reduce;
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return "";
        res = [];
        shortest_item = reduce(lambda x,y : y if len(x) > len(y) else x,strs);
        for i in range(len(shortest_item)):
            strs_set = set(map(lambda x : x[:i+1],strs));
            if len(strs_set) == 1:
                res.append(shortest_item[i]);
            else:
                return "".join(res);
        return "".join(res);