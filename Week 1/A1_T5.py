 # Calculate the area of a wall 
print ("Calculate the area of a wall.")

Feed= float(input("Enter the width in meters: "))
Width = round(Feed) 
Feed1 = float(input("Enter the height in meters: "))
Height = round(Feed1)

print("The info you entered are: ")
print("Width is {0} m and height is {1} m.".format(int(Width), int(Height)))
Area = int(Width * Height)
print("The wall will be {0} square meters.".format(Area))
