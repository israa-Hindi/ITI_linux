

x=input("enter your name : \n")
z=input("yor Age : \n")
y=input("and your faculty: \n")

# Open a file for writing
file = open("lab10", "w")

# Write some text to the file
file.write(x)
file.write("\n")
file.write(z)
file.write("\n")
file.write(y)
#file.write("")

# Close the file
file.close()