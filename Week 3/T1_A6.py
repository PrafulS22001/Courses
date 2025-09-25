print ("Program starting.")
print ("Welcome to the unit converter program!")
print("Follow the menu instructions below. \n")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print ("\nLength options:")
    print ("1 - Meters to kilometers")
    print ("2 - Kilometers to meters")
    print ("0 - Exit")
    choice = int(input("Your choice: "))
    if choice == 1: 
        meters = float (input ("Insert meters: "))
        kilometer = meters / 1000
        print (f"{meters} m is {kilometer} km")
    elif choice == 2: 
        kilometer = float (input ("Insert kilometers: "))
        meters = kilometer * 1000
        print (f"{kilometer} km is {meters} m")
    elif choice == 0:
        print ("Exiting...")
    else:
        print ("Unknown option.")
elif choice == 2: 
    print ("\nWeight options:")
    print ("1 - Grams to pounds")
    print ("2 - Pounds to grams")
    print ("0 - Exit")
    choice = int(input ("Your choice: "))
    if choice == 1: 
        grams = float (input ("Insert grams: "))
        pounds = round(grams / 453.6, 1)
        print (f"{grams} g is {pounds} lb")
    elif choice == 2:
        pounds = float (input ("Insert pounds: "))
        grams = round (pounds * 453.6 ,1)
        print (f"{pounds} lb is {grams} g")
    elif choice == 0:
        print ("Exiting...")
    else:
        print ("Unknown option.")
elif choice == 0:
    print ("Exiting...")
else: 
    print ("Unknown option.")

print ("\nProgram ending.")