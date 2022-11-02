'''
Name: 203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
Task: удалите все узлы связанного списка, у которого есть Node.val == val, и верните новый head.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        current=ListNode
        current.next=head
        prev=current
        while prev.next:
            if prev.next.val==val:
                prev.next=prev.next.next
            else:
                prev=prev.next
        current=current.next
        return current