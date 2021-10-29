"""
Fibonacci


The Fibonacci sequence is one of the most famous formulas in mathematics.
Each number in the sequence is the sum of the two numbers that precede it.
For example, here is the Fibonacci sequence for 10 numbers, starting from 0: 0,1,1,2,3,5,8,13,21,34.

Write a program to take N (variable num in code template) positive numbers as input, and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).
"""
num = int(input())


def fibonacci(n):
    #complete the recursive function
	from functools import reduce

	fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
								range(n-2), [0, 1])

	x = fib(n)
	for i in x:
		print(i)
		

fibonacci(num)
