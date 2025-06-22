# Built-in modules
import datetime
import random
import math

# 1. Show the current date and time
now = datetime.datetime.now()
print("Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 2. Pick a random number between 1 and 10
rand_num = random.randint(1, 10)
print("Random number (1–10):", rand_num)

# 3. Find the square root of a number
num = 16
sqrt_val = math.sqrt(num)
print("Square root of", num, "is", sqrt_val)

# Plotting with matplotlib (external library)
# Make sure you have matplotlib installed: pip install matplotlib

import matplotlib.pyplot as plt
import math

# Make x and y values for the sine wave
x_values = []
y_values = []

x = 0.0
while x <= 10.0:
    x_values.append(x)
    y_values.append(math.sin(x))
    x += 0.1  # increase x a little each time

# Draw the line graph
plt.plot(x_values, y_values, label='y = sin(x)', color='blue')
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
