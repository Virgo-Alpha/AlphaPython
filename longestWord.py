"""
Longest Word


Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
Recall the split(' ') method, which returns a list of words of the string.
"""

txt = input()

#your code goes here
a = txt.split()
b = max(a, key=len)

print(b)


