# Create a Python program to convert Fahrenheit to Celcius. Round the Celsius to 1 decimal precision.

# Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

# Example program run:

# Program starting.
# Insert fahrenheits: 50
# 50.0°F is 10.0°C
# Program ending.

print ("Program starting.")

fah = float (input ("Insert fahrenheits:  "))
cel = round ((fah -32)/1.8, 1)
print (f"{fah}°F is {cel}°C")

print ("Program ending.")