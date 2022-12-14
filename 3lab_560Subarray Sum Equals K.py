'''
Name: 560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
Task: Учитывая массив целых чисел nums и целое число k, верните общее количество подмассивов, сумма которых равна k.
Подмассив - это непрерывная непустая последовательность элементов внутри массива.
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        cur_sum=0
        prefix_sum={0:1}
        for item in nums:
            cur_sum+=item
            diff=cur_sum-k
            res+=prefix_sum.get(diff,0)
            prefix_sum[cur_sum]=1+prefix_sum.get(cur_sum,0)
        return res