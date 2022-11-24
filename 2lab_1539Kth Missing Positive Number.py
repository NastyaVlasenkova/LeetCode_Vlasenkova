'''
Name: 1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/
Task: Дан массив arr из натуральных чисел, отсортированных в строго возрастающем порядке, и целое число k.
Возвращает k-е положительное целое число, отсутствующее в этом массиве.
'''

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        right=len(arr)
        while left<right:
            middle=(left+right)//2
            count=arr[middle]-middle-1
            if count<k:
                left=middle+1
            else:
                right=middle
        if right==0:
            return k
        mis=arr[right-1]-right
        return arr[right-1]+k-mis
