print( 2+3*(36/9+1)**2-1)

"""
Explanation:
In this expression, () has the highest precedence. So, (36/9+1) computes
first. In this sub-expression, / has higher precedence than +. So, it results in
4.0+1=5.0 and the resultant expression becomes 2+3*5.0**2-1
In this expression, ** has the highest precedence. So, 5.0*2 will
compute now. It results in 25.0 and the resultant expression becomes
2+3*25.0-1
In this expression, * has the highest precedence. So, 3*25.0 will
compute now. It results in 75.0 and the resultant expression becomes
2+75.0-1
Now + and – has the same precedence in the resultant expression.
Both these operators are left-associative (evaluates from left to right). So, the
addition will be done first and the resultant expression becomes 77.0-1,
which produces the final output as 76.0
"""

print(3+2&4|2)

"""
In this expression, + has the highest precedence, then & and the |. So, the
expression evaluates as follows:
3+2&4|2
=5&4|2
=4|2
=6
"""