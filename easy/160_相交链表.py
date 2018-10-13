# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l_a,l_b = [],[];
        while headA:
            l_a.append(headA);
            headA = headA.next;
            
        while headB:
            l_b.append(headB);
            headB = headB.next;
        
        inter = None;
        while len(l_a) > 0 and len(l_b) > 0:
            if l_a[-1] == l_b[-1]:
                inter = l_a.pop();
                l_b.pop();
            else:
                return inter;
        
        return inter;