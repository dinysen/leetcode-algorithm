# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#笨比办法
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1,num2 = 0,0;
        tmp1,tmp2 = [],[];
        while l1:
            tmp1.insert(0,str(l1.val));
            l1 = l1.next;
        num1 = int("".join(tmp1));
        
        while l2:
            tmp2.insert(0,str(l2.val));
            l2 = l2.next;
        num2 = int("".join(tmp2));
        
        tmp3 = str(num1+num2);
        
        h = ListNode(0);
        tmp_h = h;
        for i in tmp3[::-1]:
            t_h = ListNode(i);
            tmp_h.next = t_h;
            tmp_h = tmp_h.next;
        return h.next;