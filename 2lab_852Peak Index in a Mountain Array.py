'''
Name: 852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
Task: Массив представляет собой гору, если выполняются следующие свойства. Вернуть вершину горы.
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        while left<=right:
            middle=(left+right)//2
            if (arr[middle]>arr[middle+1])and (arr[middle]>arr[middle-1]):
                return middle
            elif arr[middle]>arr[middle-1]:
                left=middle
            else:
                right=middle
