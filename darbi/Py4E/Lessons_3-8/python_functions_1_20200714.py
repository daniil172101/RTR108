import math
print(math)

signal_power=10
noise_power= 4
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels)

radians = 0.7
height = math.sin(radians)
print(height)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians))
