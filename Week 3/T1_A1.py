print ("Program starting.")
print ("Insert two interegs.")

num1 = int (input ("Insert first integer: "))
num2 = int (input ("Insert second integer: "))

print ("Comparing inserted integers. ")
if num1 > num2:
    print ("First integer is greater. \n")
elif num1 < num2: 
    print ("Second integer is greater. \n")
else:
    print ("Both integers are equal. \n")

print ("Adding integers together.")

sum = num1 + num2
print (f"{num1} + {num2} = {sum} \n")

print ("Checking the parity of the sum. . .")

if sum % 2 == 0:
    print ("Sum is even.")
else: 
    print ("Sum is odd.")

print ("Program ending.")
