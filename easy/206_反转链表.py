# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        迭代法
        建立两条链，上面的是原链，下面的是反转后的链
        等于是上下有两个指针，分别指向两条链的表头，然后上面的表头变成下面的表头，指针随之移动
        prev = None;
        while head : 
            tmp = head.next;
            head.next = prev;
            prev = head;
            head = tmp;
        return prev;
        """
        """
        递归法
        1.写出每个单元的核心程序
        2.注意核心程序中用到的方法参数，要不断进行下一次运算
        3.找出边界条件，最好就从最小范围开始找
        """
        if head == None or head.next == None:
            return head;
        h = self.reverseList(head.next);
        head.next.next = head;
        head.next = None;
        return h;