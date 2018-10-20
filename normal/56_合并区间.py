# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [];
        inter_sorted = sorted(intervals,key = lambda x : x.start);
        res = [];
        cur = None;
        i = 0;
        while len(inter_sorted) != 0:
            inter = inter_sorted.pop(0);
            if not cur:
                cur = inter;
            else:
                if cur.end < inter.start:
                    res.append(cur);
                    cur = inter;
                if cur.start <= inter.end:
                    cur.end = inter.end if inter.end >= cur.end else cur.end;
        res.append(cur);
        return res;
            