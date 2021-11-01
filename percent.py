"""
Letter Frequency


You are making a program to analyze text.
Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

Sample Input:
hello
l

Sample Output:
40

The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.
Division result is a float. Use the int() function to convert the result to an integer.
"""

#your code goes here
text1 = input()
text2 = input()
count = 0

for i in text1:
    if i == text2:
        count += 1

freq = int((count/(len(text1)))*100)

print(freq)
