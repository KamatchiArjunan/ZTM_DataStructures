#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    n1 = len(s1)
    n2 = len(s2)
    cnt = 0
    if n1 <= n2:
        n3 = n2
        for i in range(n1):
            j = 0
            while j < n2:
                if s2[j] == s1[i]:
                    cnt += 1
                    s2 = s2[:j]+s2[j+1:]
                    n2 -= 1
                    break
                j += 1
        total = (n1 + n3 - (2*cnt))
        return (total)
    else:
        n4 = n1
        for i in range(n2):
            j = 0
            while j < n1:
                if s1[j] == s2[i]:
                    cnt += 1
                    s1 = s1[:j] + s1[j + 1:]
                    print(s1)
                    n1 -= 1
                    break
                j += 1
        total = (n4 + n2 - (2 * cnt))
        return (total)


if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(result)
