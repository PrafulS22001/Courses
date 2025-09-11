# print ("he said hello\\' and kept walking")
# print ('he said hello\' and \n kept walking') #\n is used to print in new line
# print ("he said hello\" and \t kept walking") #\t is used to give a tab space
# print ("he said hello\\ and \r kept walking") #\r is used to return to the begining of the line

# name = input ("Enter your name: ")
# print ("Hello "+ name[0] )
# print ("Hello "+ name[-2] )
Sentence = "Praful Sharma"
print (Sentence[-2])   #print the second last character of the string
print (Sentence[2:9]) # print from index 2 to 8 
print (Sentence[:9]) # print from index 0 to 8
print (Sentence[-9:-2]) #print from index -9 to -3
print (Sentence[2:9:3]) #print from index 2 to 8 with each 3rd character
print (Sentence[::3]) #prints from index 0 to 3 with each 3rd character till the end of the string
print (Sentence[::-1])  #print the string in reverse order

exString = "Hello" #string value  
exInt = 2 # integer 
exBool = True #true or false 
exFloat = 3.14 #floaring value i.e decimal value

print (123 + 456 ) #prints the addtion. 0
 
calclength = len (Sentence) #len function gives the length of the string    

num3 = 10 
num4 = float(num3) # when printing; it print 10.0 

roundMe = round(8/3,2) #rounds the value to 2 decimal places

Name = "Praful"
Age = 19 
formatted = "My name is %s and my age is %d" %(Name,Age)  #old way of formatting #%s is for string and %d is for integer 
print (formatted)
formatted2 = "My name is {} and my age is {}".format(Name,Age) #new way of formatting
print (formatted2)

float1 = 3.14159
format = "The valaue of this is %f" %(float1) #prints 6 decimal places by default
print (format)

format2 = "My name is {0} and my age is {1} and I scored {2:.2f} in maths".format(Name,Age, float1) #prints each value in the order of index and .2f is used to print 2 decimal places
print (format2)

