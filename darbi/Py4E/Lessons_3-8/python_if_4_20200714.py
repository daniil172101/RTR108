#This script compare integers in x and y variables (nested conditionals)

a = input('Enter x\n')
x = int(a)

b = input('Enter y\n')
y = int(b)

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
