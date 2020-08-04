# In this example, because strings are immutalbe,
# first letter of 'greeting' variable can't be changed.
# That is why a new string was created, which is a variation on the original.
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)
