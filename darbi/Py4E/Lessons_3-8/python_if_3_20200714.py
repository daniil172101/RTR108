# This script compare integers in x and y variables (chained conditionals)

a = input('Enter x\n')
x = int(a)

b = input('Enter y\n')
y = int(b)

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

