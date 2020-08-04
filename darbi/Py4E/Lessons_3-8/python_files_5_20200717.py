# This script opens file 'mbox-short.txt'
# and shows lines which contain the string "@uct.ac.za"
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)
