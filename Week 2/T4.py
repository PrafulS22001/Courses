# Prompt the user to insert the minutes spent on each previous topic task. Calculate the sum and the average. Display those in the example program run format(Note! precision). Make sure to calculate the required average for two decimal digits and later integer as rounded integer (precision 0 + type conversion).

# Example program run:

# Program starting.
# Estimate how many minutes you spent on programming...

# A1_T1: 3
# A1_T2: 7
# A1_T3: 9
# A1_T4: 8
# A1_T5: 13
# A1_T6: 14
# A1_T7: 21

# In total you spent 75 minutes on programming.
# Average per task was 10.71 min and same rounded to the nearest integer 11 min.

# Program ending.

print ("Program starting.")
print ("Estimate how many minutes you spent on programming...\n")

A1_T1 = int(input("A1_T1: "))
A1_T2 = int(input("A1_T2: "))
A1_T3 = int(input("A1_T3: "))
A1_T4 = int(input("A1_T4: "))
A1_T5 = int(input("A1_T5: "))
A1_T6 = int(input("A1_T6: "))
A1_T7 = int(input("A1_T7: "))

total = A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7
average = total / 7
average_rounded = round(average)
print (f"\nIn total you spent {total} minutes on programming.")
print (f"Average per task was {average:.2f} min and same rounded to the nearest integer {average_rounded} min.")
print ("\nProgram ending.")
# #print(len(.....))
# Program starting.