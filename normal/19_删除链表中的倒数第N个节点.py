#/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

#解答：

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = ListNode(0);
        first.next = head;
        prevNode = curNode = first;
        
        for i in range(n):
            curNode = curNode.next;
        
        while curNode.next:
            prevNode = prevNode.next;
            curNode = curNode.next;
        prevNode.next = prevNode.next.next;
        
        return first.next;