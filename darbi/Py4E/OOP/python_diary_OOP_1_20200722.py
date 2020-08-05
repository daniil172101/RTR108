stuff = list()              # Construct an object of type list
stuff.append('python')      # Adds in a list an item 'python'
stuff.append('chuck')       # Adds in a list an item 'chuck'
stuff.sort()                # Sort list in alphabetical order

# The next 3 lines prints the item of a list with a parameter of zero.
print (stuff[0])
print (stuff.__getitem__(0))
print (list.__getitem__(stuff,0))
