# This script opens file for writing
# and writes 2 lines to the file.
# (If the file already exists, opening it in write mode clears out the old data
# and starts fresh. If the file doesn’t exist, a new one is created.)
fout = open('output.txt', 'w')
print(fout)

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = 'the emblem of our land.\n'
fout.write(line2)

fout.close()
