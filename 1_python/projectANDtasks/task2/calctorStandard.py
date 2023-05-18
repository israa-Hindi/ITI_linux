def calculator():
    # Display a menu of available operations
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for operation choice
    choice = int(input("Enter choice (1-4): "))

    # Get user input for operands
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Perform the selected operation on the operands
    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        result = num1 / num2
    else:
        print("Invalid input")
        return

    # Print the result of the operation
    print(f"Result: {result}")

calculator() # Call the function to run the calculator