'''
Name: 35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
Task: верните индекс, если целевое значение найдено в массиве.
Если нет, верните индекс туда, где он был бы, если бы он был вставлен по порядку.
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(left+right)//2
            if target==nums[middle]:
                return middle
            if target>nums[middle]:
                left=middle+1
            else:
                right=middle-1
        return left