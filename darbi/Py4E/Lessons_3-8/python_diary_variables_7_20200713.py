# 'input' function gets input from the keyboard

inp = input()       # If input: Some silly stuff
print(inp)          # Output: Some silly stuff

name = input('What is your name?\n')    # If input: Chuck
print(name)                             # Output: Chuck

prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt)           # If input: 17

print(int(speed))               # Output: 17
print(int(speed) + 5)           # Output: 22


