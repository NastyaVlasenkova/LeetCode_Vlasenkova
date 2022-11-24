'''
Name: 977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
Task: Учитывая целочисленный массив чисел, отсортированных в порядке неубывания,
верните массив квадратов каждого числа, отсортированных в порядке неубывания.
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        left=0
        right=len(nums)-1
        result=[]
        while left<=right:
            if abs(nums[left])>=abs(nums[right]):
                result.append(nums[left]**2)
                left+=1
            else:
                result.append(nums[right]**2)
                right-=1
        return result[::-1]
