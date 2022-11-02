'''
Name: 2181. Merge Nodes in Between Zeros
https://leetcode.com/problems/merge-nodes-in-between-zeros/
Task: Для каждых двух последовательных 0 объедините все узлы, лежащие между ними, в один узел,
значение которого равно сумме всех объединенных узлов. Измененный список не должен содержать никаких 0.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        head = head.next
        current = head
        total = 0
        while current:
            total += current.val
            if current.val == 0:
                head = ListNode(val = total)
                head.next = self.mergeNodes(current)
                return head
            current = current.next