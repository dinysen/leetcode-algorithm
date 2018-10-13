# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
这个比较慢
class Solution:
    def oddEvenList(self, head):
        even = [];
        index = 1;
        h = ListNode(-1);
        h_tmp = h;
        while head:
            if index % 2 == 0:
                even.append(head);
            else:
                h_tmp.next = head;
                h_tmp = h_tmp.next;
            head = head.next;
            index += 1;
        for i in even:
            h_tmp.next = i;
            h_tmp = h_tmp.next;
        h_tmp.next = None;
        return h.next;
"""

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head;
        h_odd = head.next.next;
        h_even = head.next;
        head.next = h_odd;
        tmp_even = h_even;
        while h_odd.next:
            h_even.next = h_even.next.next;
            h_even = h_even.next;
            h_odd.next = h_odd.next.next;
            if h_odd.next:
                h_odd = h_odd.next;
        h_odd.next = tmp_even;
        h_even.next = None;
        return head;