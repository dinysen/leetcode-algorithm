#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
#现有一个链表 -- head = [4,5,1,9]，它可以表示为:


#解答：
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val;
        node.next = node.next.next;
