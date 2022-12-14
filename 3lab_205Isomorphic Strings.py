'''
Name: 205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
Task: Учитывая две строки s и t, определите, изоморфны ли они.
Две строки s и t изоморфны, если символы в s можно заменить, чтобы получить.
Все вхождения символа должны быть заменены другим символом с сохранением порядка символов.
Никакие два символа не могут сопоставляться с одним и тем же символом, но символ может сопоставляться сам с собой.
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_ST,map_TS={},{}
        for i,j in zip(s,t):
            if ((i in map_ST and map_ST[i]!=j) or (j in map_TS and map_TS[j]!=i)):
                return False
            map_ST[i]=j
            map_TS[j]=i
        return True