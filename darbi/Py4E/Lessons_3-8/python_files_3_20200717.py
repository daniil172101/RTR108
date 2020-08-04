# This script is similar to the previous script, but it uses 'line.rstrip()'
# to remove extra blank lines in the output
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
