#!/usr/bin/env python
"""
Daily Coding Problem: Problem #1

This problem was recently asked by Google:
* Given a list of numbers and a number k,
* return whether any two numbers from the list add up to k.
*
* For example, given [10, 15, 3, 7] and k of 17,
* return true since 10 + 7 is 17.
"""

def sum_of_pairs(list, k):
    for i in range(0, len(list)):
        for j in range (i, len(list)):
            if (list[i] + list[j] == k):
                return True
    return False

if __name__ == '__main__':
    result = sum_of_pairs([10, 15, 3, 7], 17)
    print(result)
