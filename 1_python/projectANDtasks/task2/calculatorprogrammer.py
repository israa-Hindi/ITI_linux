def decimal_to_hexadecimal(decimal_num):
    hexadecimal_num = hex(decimal_num)
    return hexadecimal_num

def decimal_to_octal(decimal_num):
    octal_num = oct(decimal_num)
    return octal_num

def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)
    return binary_num

def hexadecimal_to_decimal(hexadecimal_num):
    decimal_num = int(hexadecimal_num, 16)
    return decimal_num

def octal_to_decimal(octal_num):
    decimal_num = int(octal_num, 8)
    return decimal_num

def binary_to_decimal(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_num

# Display a menu of available conversion options
print("Select conversion:")
print("1. Decimal to Hexadecimal")
print("2. Decimal to Octal")
print("3. Decimal to Binary")
print("4. Hexadecimal to Decimal")
print("5. Octal to Decimal")
print("6. Binary to Decimal")

# Get user input for conversion choice
choice = int(input("Enter choice (1-6): "))

# Get user input for the number to convert
num = input("Enter the number to convert: ")

# Perform the selected conversion
if choice == 1:
    decimal_num = int(num)
    result = decimal_to_hexadecimal(decimal_num)
elif choice == 2:
    decimal_num = int(num)
    result = decimal_to_octal(decimal_num)
elif choice == 3:
    decimal_num = int(num)
    result = decimal_to_binary(decimal_num)
elif choice == 4:
    hexadecimal_num = num
    result = hexadecimal_to_decimal(hexadecimal_num)
elif choice == 5:
    octal_num = num
    result = octal_to_decimal(octal_num)
elif choice == 6:
    binary_num = num
    result = binary_to_decimal(binary_num)
else:
    print("Invalid input")
    exit()

# Print the result of the conversion
print(f"Result: {result}")