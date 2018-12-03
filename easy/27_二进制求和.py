import collections;
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        list_a = collections.deque(list(a));
        list_b = collections.deque(list(b));
        len_diff = len(list_a) - len(list_b);
        if len_diff > 0:
            for i in range(len_diff):
                list_b.appendleft(0);
        elif len_diff < 0:
            for i in range(-len_diff):
                list_a.appendleft(0);
        carry = 0;
        res = [];
        for i in range(len(list_a)-1,-1,-1):
            print(i,int(list_a[i]) , int(list_b[i]) , carry);
            tmp = int(list_a[i]) + int(list_b[i]) + carry;
            res.append(str(tmp % 2));
            carry = tmp // 2;
        if carry == 1:
            res.append("1");
        return "".join(res[::-1]);
            