'''
Name: 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
Task: Учитывая массив строк strs, сгруппируйте анаграммы вместе. Вы можете вернуть ответ в любом порядке.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=defaultdict(list)
        for item in strs:
            count=[0]*26
            for i in item:
                count[ord(i)-ord("a")]+=1
            res[tuple(count)].append(item)
        return res.values()