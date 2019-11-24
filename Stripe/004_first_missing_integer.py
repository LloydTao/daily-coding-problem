#!/usr/bin/env python
"""
Daily Coding Problem: Problem #4

This problem was asked by Stripe:
* Given an array of integers, find the first missing positive 
* integer in linear time and constant space. In other words, 
* find the lowest positive integer that does not exist in the array.
* 
* For example, the input [3, 4, -1, 1, 3] should give 2.
"""

def first_missing_integer(list):
  
    # Assume 'smallest' is larger than all elements, 
    smallest = max(list) + 1
    
    # Iterate from zero until an integer is found to be missing.
    for i in range(1, smallest):
        exists = False
        for j in range(0, len(list)):
            print ("Comparing", i, " to ", list[j])
            if (i == list[j]):
                exists = True
                break
        if (exists):
            continue
        smallest = i
        break
        
    # Value of 'smallest' will be negative if whole list was negative.
    if (smallest < 1):
        smallest = 1
    return smallest

if __name__ == '__main__':
    result = first_missing_integer([3, 4, -1, 1, 3])
    print(result)
    result = first_missing_integer([-3, -4, -2])
    print(result)
