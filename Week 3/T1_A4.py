print ("Program starting.")
print ("This is a program with simple menu, where you can choose which operation the program performs.")

Name = input ("Before the menu, please insert your name: ")

print ("\nOptions: ")
print ("1 - Print welcome message \n2 - Print the name backwards\n3 - Print the first character\n4 - Show the amount of characters in the name\n0 - Exit")

backwards = Name[::-1]
First_char = Name[0]
Length = len(Name)

choice = int(input("Your choice: "))
if choice == 1: 
    print (f"Welcome {Name}! \n")
elif choice == 2: 
    print (f'Your name backwards is \"{backwards}"\ \n')
elif choice == 3: 
    print (f"The first character in name \"{Name}\" is \"{First_char}\" \n")
elif choice == 4:
    print(f"There are {Length} characters in the name \"{Name}\" \n")
elif choice == 0:
    print (f"Exiting ...\n")
else: 
    print ("Unknown option. \n")

print ("Program ending.")

