'''
Name: 75. Sort Colors
https://leetcode.com/problems/sort-colors/
Task: Учитывая числовой массив с n объектами, окрашенными в красный, белый или синий цвета,
отсортируйте их по месту так, чтобы объекты одного цвета были смежными, с цветами в порядке красного, белого и синего.
Мы будем использовать целые числа 0, 1 и 2 для представления красного, белого и синего цветов соответственно.
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)-1
        i=0

        def swap(i,j):
            nums[i],nums[j]=nums[j],nums[i]
        while i<=r:
            if nums[i]==0:
                swap(l,i)
                l+=1
            elif nums[i]==2:
                swap(i,r)
                r-=1
                i-=1
            i+=1