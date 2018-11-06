# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

----------------------------------------------------
#如果长度不一致就无限邻接
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        tmp_a = headA;
        tmp_b = headB;
        while tmp_a != None or tmp_b != None:
            if tmp_a == tmp_b:
                return tmp_a;
            tmp_a = headB if tmp_a == None else tmp_a.next;
            tmp_b = headA if tmp_b == None else tmp_b.next;
        return None;

---------------------------------------------------------

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

--------------------------------------------------
#暴力破解 LTE
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tmp_A = headA;
        tmp_B = headB;
        while tmp_A:
            while tmp_B:
                if tmp_A == tmp_B:
                    return tmp_A;
                else:
                    tmp_B = tmp_B.next;
                tmp_B = headB;
            tmp_A = tmp_A.next;
        return None;