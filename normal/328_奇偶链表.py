# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 要注意的是最后一个节点的next要置空，否则链会形成闭环，没法玩了

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l_temp = [];
        h = ListNode(0);
        h_tmp = h;
        i = 1;
        
        while head:
            if i % 2 != 0:
                h_tmp.next = head;
                h_tmp = h_tmp.next;
            else:
                l_temp.append(head);
            head = head.next;
            i += 1;
        
        for node in l_temp:
            h_tmp.next = node;
            h_tmp = h_tmp.next;
            
        h_tmp.next = None;
        
        return h.next;
                