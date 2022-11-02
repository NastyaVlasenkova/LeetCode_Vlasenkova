'''
Name: 160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
Task: Учитывая заголовки двух односвязных списков header и headB, верните узел,
в котором пересекаются два списка. Если два связанных списка вообще не пересекаются, верните значение null.
'''

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
        lst = set()
        current = headA
        while current:
            lst.add(current)
            current = current.next
        current = headB
        while current:
            if current in lst:
                return current
            current = current.next
        return None