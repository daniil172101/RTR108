import math     # This command imports math module
print(math)

signal_power=10
noise_power= 4
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)       #The first example computes the logarithm base 10 of the signal-to-noise ratio.
print(decibels)

radians = 0.7
height = math.sin(radians)              #The second example finds the sine of radians.
print(height)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))                # In this example 45 degrees are converted to radians and then script finds the sine of radians. 
