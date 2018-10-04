#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#这里特别要注意的是如何保存一个链表的方法
#cur = h; 此时h.next和cur.next指向的是同一个内存地址，但是h和cur互相独立
#所以之后再修改cur的值，不影响h，即h.next就是链表表头
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = ListNode(-1);
        cur = h;
        cur1 = l1;
        cur2 = l2;
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1;
                cur1 = cur1.next;
            else:
                cur.next = cur2;
                cur2 = cur2.next;
            cur = cur.next;
        if not cur1:
            cur.next = cur2;
        if not cur2:
            cur.next = cur1;
        return h.next;