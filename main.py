"""
Given a number n as input, calculate the sum of its digits. Use recursion. Do not use loops. Do a dry run for each test case.
Hint: n%10 gives the last digit. n/10 removes the last digit.
Input-> 234561
Output-> 21
"""

def sumDigi(num):
  sum = 0
  ld = num % 10
  if (ld == 0):
    return 0
  else:
    sum = sum + ld
  num = num / 10
  return (sum)

num = 234561
print(sumDigi(num))
