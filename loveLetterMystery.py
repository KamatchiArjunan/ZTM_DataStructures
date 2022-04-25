#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    count = 0
    #Checking if the input string is already a palindrome. if yes, return count = 0 since no moves are required
    if s == s[::-1]:
      return(count)
      
    else:
      #compute the half integer length of the given string
      n = int(len(s)/2)
      #Initialize i = starting char of the string, j = end char of the string
      j = -1
      i = 0
      #Compare the direct and reverse half of the string to find out characters which need to be replaced
      #if the values are different, take the absolute difference between their ascii values and return it as count
      while (i < n):
        if s[i] == s[j]:
          print(s[i])
          j -= 1
          i += 1
        else:
          count = count + abs(ord(s[i]) - ord(s[j]))
          j -= 1
          i += 1
      return(count)

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(result)
