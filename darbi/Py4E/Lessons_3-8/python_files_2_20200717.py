# This script opens file 'mbox-short.txt' and prints out lines
# which started with the prefix “From:”
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
 
