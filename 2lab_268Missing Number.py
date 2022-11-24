'''
Name: 268. Missing Number
https://leetcode.com/problems/missing-number/
Task: Учитывая массив nums, содержащий n различных чисел в диапазоне [0, n],
верните единственное число в диапазоне, которое отсутствует в массиве.
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)*(len(nums)+1)/2 - sum(nums)
