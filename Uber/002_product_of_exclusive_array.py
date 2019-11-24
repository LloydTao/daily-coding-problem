#!/usr/bin/env python
"""
Daily Coding Problem: Problem #2

This problem was asked by Uber:
* Given an array of integers, return a new array such that
* each element at index i of the new array is the product of
* all the numbers in the original array except the one at i.
*
* For example, if our input was [1, 2, 3, 4, 5],
* the expected output would be [120, 60, 40, 30, 24].
"""

def product_of_exclusive_array(list):
    new_list = []
    for i in range(0, len(list)):
        value = 1
        for j in range(0, i):
            value = value * list[j]
        for j in range(i+1, len(list)):
            value = value * list[j]
        new_list.append(value)
    return new_list

if __name__ == '__main__':
    result = product_of_exclusive_array([1, 2, 3, 4, 5])
    print(result)
