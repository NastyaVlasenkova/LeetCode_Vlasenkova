'''
Name: 441. Arranging Coins
https://leetcode.com/problems/arranging-coins/
Task: У вас есть n монет, и вы хотите построить лестницу из этих монет.
Лестница состоит из k рядов, где в i-м ряду ровно i монет. Последний ряд лестницы может быть неполным.
Учитывая целое число n, верните количество полных рядов лестницы, которую вы будете строить.
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left=1
        right=n
        res=0
        while left<=right:
            middle=(left+right)//2
            coins=(middle/2)*(middle+1)
            if coins>n:
                right=middle-1
            else:
                left=middle+1
                res=max(middle,res)
        return res
