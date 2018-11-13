# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.

# !/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum, a, b = 0, 0, 1
    while b < n:
        if b % 2 == 0:
            sum += b
        a, b = b, a + b
    print(sum)