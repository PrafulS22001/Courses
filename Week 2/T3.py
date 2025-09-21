# #print(len(.....))
# Program starting.
# Insert first word: fire
# Insert second word: fighter
# 1st word is 4 characters long.
# 2nd word is 7 characters long.
# Words together makes one closed compound 'firefighter'.
# Program ending.

print ("Program starting.")
word1 = input ("Insert first word: ")
word2 = input ("Insert second word: ")  
len1 = len(word1)
len2 = len(word2)
print (f"1st word is {len1} characters long.")
print (f"2nd word is {len2} characters long.")
print (f"Words together makes one closed compound \'{word1}{word2}\'.")
print ("Program ending.")