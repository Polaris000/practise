"""
This code takes a normal natural number (base 10)
and converts it to binary (base 2)

Input:
A single integer (var a)

Method:
To convert an number from decimal to binary, repeatedly 
divide your base 10 number, x, by 2. The dividend at each step  
should be the result of the integer division at each step.
The remainder at each step of division is a single digit 
of the binary equivalent of x; if you then read each remainder
in order from the last remainder to the first (demonstrated below),
you have the entire binary number.

Output:
A continuous binary number (var binary-- a list)

Sample:
Input:
3

Ouput:
11

Explanation:

3 % 2 = 1
3 // 2 = 1

1 % 2 = 1
Binary = 11
"""

a = int(input())

d = a
reverse_binary = []

while d >= 1:
   reverse_binary.append(d % 2)
   d //= 2

# inverting current list to form the actual list
binary = reverse_binary[::-1]  

for i in binary:
   print(i,end='')
   
print(" \n")