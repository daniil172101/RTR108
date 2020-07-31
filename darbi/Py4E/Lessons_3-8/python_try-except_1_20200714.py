#This script converts a Fahrenheit temperature to a Celsius temperature
# and uses 'try-except' to protect script from invalid input

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
