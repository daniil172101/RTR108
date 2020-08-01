# This script uses 'while' statement with 'break' to exit loop if user inputs 'done'
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
