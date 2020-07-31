#This script is example of short-circuit evaluation of logical expressions

a = input('Enter x\n')
x = int(a)

b = input('Enter y\n')
y = int(b)

print(x >= 2 and y != 0 and (x/y) > 2)
