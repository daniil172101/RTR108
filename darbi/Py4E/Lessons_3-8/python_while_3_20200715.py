# This script uses 'continue' to skip to the next iteration
# without finishing the body of the loop for the current iteration
# if first symbol is '#',
# and uses 'break' to exit loop if user inputs 'done'
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
