# This script is a simple version
# of the Python built-in 'min()' function
def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

print(min([3, 41, 12, 9, 74, 15]))
