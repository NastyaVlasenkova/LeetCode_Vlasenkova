'''
Name: 1. Two Sum
https://leetcode.com/problems/two-sum/
Task: Учитывая массив целых чисел nums и целочисленное целевое значение,
верните индексы двух чисел таким образом, чтобы они складывались в target.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        values={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in values:
                result.append(values[diff])
                result.append(i)
            else:
                values[n]=i
        return result