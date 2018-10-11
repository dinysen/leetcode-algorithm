class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {};
        l = [];
        for i in strs:
            sor = "".join(sorted(i));
            if sor in d:
                l[d[sor]].append(i);
            else:
                d[sor] = len(l);
                l.append([i]);
        return l;