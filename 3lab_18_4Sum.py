'''
Name: 18. 4Sum
https://leetcode.com/problems/4sum/
Task: Учитывая массив nums из n целых чисел,
верните массив всех уникальных четверок [nums[a], nums[b], nums[c], nums[d]] таких, что:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
'''

class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            a = nums[i]
            for j in range(i + 1, n - 2):
                b = nums[j]
                left = j + 1
                right = n - 1
                while left < right:
                    c = nums[left]
                    d = nums[right]
                    total = b + c + d
                    if total == target - a:
                        res.add(tuple([a, b, c, d]))
                        left += 1
                        right -= 1
                    elif total > target - a:
                        right -= 1
                    else:
                        left += 1
        return list(res)
