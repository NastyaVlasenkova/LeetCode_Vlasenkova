'''
Name: 1893. Check if All the Integers in a Range Are Covered
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
Task: Вам дается 2D целочисленный массив диапазонов и два целых числа слева и справа.
Возвращает значение true, если каждое целое число во включающем диапазоне [слева, справа]
покрыто по крайней мере одним интервалом в диапазонах.
В противном случае верните значение false.
'''

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        count = 0
        for i in range(left, right + 1):
            for l, r in ranges:
                if l <= i <= r:
                    count += 1
                    break
        return count == right - left + 1