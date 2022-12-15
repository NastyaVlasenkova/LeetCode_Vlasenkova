'''
Name: 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
Task: Учитывая массив строк strs, сгруппируйте анаграммы вместе. Вы можете вернуть ответ в любом порядке.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())