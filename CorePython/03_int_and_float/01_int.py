# Integer Datatype in python.

a = 10
print(type(a)) # <class 'int'>

# Arithmetic Operations:
'''
1. Addition
2. Multiplication
3. Substraction
4. Division
5. Modulus -> returns remainder value. Operator: %
6. Floor Division -> Division + Round to floor value. Operator: //
7. Exponent -> power. Operator: **
'''

assert 3/2 == 1.5
assert 3//2 == 1 # Floor value
assert 3**2 == 9
assert 7 % 5 == 2

# Some methods in integer datatype.
# Check the methods through dir(int)

# 1. abs() gives the absolute value - postive integer.
print(abs(-3))

# 2. pow(element, power)
print(pow(2, 4)) # 16

# Type casting.
num1 = '100'
num2 = '200'
print(num1 + num2) # 100200
print(int(num1) + int(num2)) # 300