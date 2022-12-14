'''
Name: 237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/
Task: Существует односвязный заголовок списка, и мы хотим удалить узел node в нем.
Вам дается узел, который будет удален узлом. Вам не будет предоставлен доступ к первому узлу head.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next;