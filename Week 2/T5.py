#Make a Python program, which prompts for a compound word.

# Get following aspects from the word
# Length
# First character
# Reversed version e.g. “Suitcase” is reversed “esactiuS”
# Display the aspects using print commands.
# Prompt the user to take substring from the existing compound word.
# Finally print the user specified substring.
# Example program run:

# Program starting.

# Insert a closed compound word: Moonbanana
# The word you inserted is 'Moonbanana' and in reverse it is 'ananabnooM'.
# The inserted word length is 10
# Last character is 'a'

# Take substring from the inserted word by inserting...
# 1) Starting point: 0
# 2) Ending point: 4
# 3) Step size: 1

# The word 'Moonbanana' sliced to the defined substring is 'Moon'.
# Program ending.

print ("Program starting. \n") 

Word = input ("Insert a closed compound word: ")
Len = len (Word)
One = Word[0]
Reverse = Word[::-1]
final= Word[-1] 

print (f"The word you inserted is \'{Word}\' and in reverse it is \'{Reverse}\'." )
print (f"The inserted word length is {Len}")
print (f"Last character is \'{final}\' \n")

print ("Take substring from the inserted word by inserting... ")
S_Point = int (input ("1) \t Starting point: "))
E_Point = int (input ("2) \t Ending point: "))
St_Point = int (input ("3) \t Step point: "))

Substr = Word [S_Point:E_Point:St_Point]

print (f"\nThe word \'{Word}\' sliced to the defined substring is \'{Substr}\'.")
print ("Program ending.")