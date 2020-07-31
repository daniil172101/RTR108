import random

for i in range(10):         
    x = random.random()
    print(x)            # This program produces the list of 10 random numbers between 0.0 and up to but not including 1.0.


print(random.randint(5, 10))        # The function 'randint' takes the parameters 'low' and 'high', and returns an integer between 'low' and 'high' (including both).

t = [1, 2, 3]
print(random.choice(t))         # To choose an element from a sequence at random, 'random.choice' can be used
