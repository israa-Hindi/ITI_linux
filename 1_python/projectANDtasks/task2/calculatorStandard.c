
#include <stdio.h>

void calculator();

int main() {
    calculator();
    return 0;
}

void calculator() {
    // Display a menu of available operations
    printf("Select operation:\n");
    printf("1. Add\n");
    printf("2. Subtract\n");
    printf("3. Multiply\n");
    printf("4. Divide\n");

    // Get user input for operation choice
    int choice;
    printf("Enter choice (1-4): ");
    scanf("%d", &choice);

    // Get user input for operands
    int num1, num2;
    printf("Enter first number: ");
    scanf("%d", &num1);
    printf("Enter second number: ");
    scanf("%d", &num2);

    // Perform the selected operation on the operands
    int result;
    if (choice == 1) {
        result = num1 + num2;
    }
    else if (choice == 2) {
        result = num1 - num2;
    }
    else if (choice == 3) {
        result = num1 * num2;
    }
    else if (choice == 4) {
        result = num1 / num2;
    }
    else {
        printf("Invalid input\n");
        return;
    }

    // Print the result of the operation
    printf("Result: %d\n", result);
}