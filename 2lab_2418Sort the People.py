'''
Name: 2418. Sort the People
https://leetcode.com/problems/sort-the-people/
Task: Вам дается массив имен строк и массив высот, состоящий из различных целых положительных чисел.
Оба массива имеют длину n.
Возвращает имена, отсортированные в порядке убывания по росту людей.
'''


def sorting(heights):
    if len(heights) <= 1:
        return heights
    left = []
    right = []
    center = []
    elem = heights[0][1]
    for item in heights:
        if item[1] < elem:
            left.append(item)
        elif item[1] > elem:
            right.append(item)
        else:
            center.append(item)

    return sorting(right) + center + sorting(left)


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new_array = [(n, h) for n, h in zip(names, heights)]
        res = sorting(new_array)
        return [n for n, h in res]
