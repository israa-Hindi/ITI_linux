
while True:
    print("1 zfill()\n2 upper()\n3 translate()\n ")
    Name=input("enter num of fun you want to understand its mechanizm\n")

    if Name == "1":
            x="hellow"
            print("\nThe zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.")
            print(" if we have x= 'hellow'and do x.zfill(10) then the output is :  ")
            print(x.zfill(10))

    elif Name == "2":
            x="hellow"
            print("\nThe upper() method returns a string where all characters are in upper case")
            print("if we have x= 'hellow' and do x.upper() then the output is :  ")
            print(x.upper())
                
    elif Name == "3":

            x="Hello Sam!"
            print("\nThe translate() method returns a string whit specific exchages")
            print(" if we have x= 'Hello Sam!' and do x.translate() then the output is :  ")
            txt = "Hello Sam!"
            mytable = str.maketrans("S", "P")
            print(txt.translate(mytable))
    else:
            print("Invalid input")
            break;