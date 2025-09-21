# Program starting.
# What is your name: John
# Enter a floating point number: 3.1
# Enter second floating point number: 5.3
# John you gave numbers 3.1 and 5.3
# Multiplying first and second number will result in product 16.43
# Program ending.


print ("Program starting.")
name = input ("What is your name:  ")
Point1 = float (input ("Enter a floating point number: "))
Point2 = float (input ("Enter second floating point number: "))

print (f"{name} you gave numbers {Point1} and {Point2}")
Product = Point1 * Point2
print (f"Multiplying first and second number will be result in product {round(Product,2)}")
print ("Program ending.")