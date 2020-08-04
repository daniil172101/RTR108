#This script opens file 'mbox-short.txt' and counts lines in file

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
