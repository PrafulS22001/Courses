print ("Program starting.")

print ("String Comparision.")

Word1 = input ("Insert first word: ")
char1 = input ("Insert a character: ")

if Word1 in char1:
    print(f"Word \"{Word1}\" contains character \"{char1}\". ") 
else: 
    print(f"Word \"{Word1}\" does not contain character \"{char1}\". ")

Word2 = input ("Insert second word: ")

if Word1 > Word2:
    print (f"The first word \"{Word1}\" is before the second word \"{Word2}\" in alphabetically.")
elif Word1 < Word2:
    print (f"The second word \"{Word2}\" is before the first word \"{Word1}\" in alphabetically.")
else:
    print (f"Both inserted words are the same alphabetically, {Word1}\n")

print ("Program ending.")
