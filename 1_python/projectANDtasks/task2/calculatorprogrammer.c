#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * decimal_to_hexadecimal(int decimal_num);
char * decimal_to_octal(int decimal_num);
char * decimal_to_binary(int decimal_num);
int hexadecimal_to_decimal(char * hexadecimal_num);
int octal_to_decimal(char * octal_num);
int binary_to_decimal(char * binary_num);

int main() {
    // Display a menu of available conversion options
    printf("Select conversion:\n");
    printf("1. Decimal to Hexadecimal\n");
    printf("2. Decimal to Octal\n");
    printf("3. Decimal to Binary\n");
    printf("4. Hexadecimal to Decimal\n");
    printf("5. Octal to Decimal\n");
    printf("6. Binary to Decimal\n");

    // Get user input for conversion choice
    int choice;
    printf("Enter choice (1-6): ");
    scanf("%d", &choice);

    // Get user input for the number to convert
    char num[100];
    printf("Enter the number to convert: ");
    scanf("%s", num);

    // Perform the selected conversion
    char * result;
    switch (choice) {
        case 1:
            result = decimal_to_hexadecimal(atoi(num));
            break;
        case 2:
            result = decimal_to_octal(atoi(num));
            break;
        case 3:
            result = decimal_to_binary(atoi(num));
            break;
        case 4:
            result = malloc(sizeof(char) * 100);
            sprintf(result, "%d", hexadecimal_to_decimal(num));
            break;
        case 5:
            result = malloc(sizeof(char) * 100);
            sprintf(result, "%d", octal_to_decimal(num));
            break;
        case 6:
            result = malloc(sizeof(char) * 100);
            sprintf(result, "%d", binary_to_decimal(num));
            break;
        default:
            printf("Invalid input\n");
            exit(1);
    }

    // Print the result of the conversion
    printf("Result: %s\n", result);

    // Free the allocated memory
    free(result);

    return 0;
}

char * decimal_to_hexadecimal(int decimal_num) {
    char * hexadecimal_num = malloc(sizeof(char) * 100);
    sprintf(hexadecimal_num, "%X", decimal_num);
    return hexadecimal_num;
}

char * decimal_to_octal(int decimal_num) {
    char * octal_num = malloc(sizeof(char) * 100);
    sprintf(octal_num, "%o", decimal_num);
    return octal_num;
}

char * decimal_to_binary(int decimal_num) {
    char * binary_num = malloc(sizeof(char) * 100);
    itoa(decimal_num, binary_num, 2);
    return binary_num;
}

int hexadecimal_to_decimal(char * hexadecimal_num) {
    int decimal_num;
    sscanf(hexadecimal_num, "%X", &decimal_num);
    return decimal_num;
}

int octal_to_decimal(char * octal_num) {
    int decimal_num;
    sscanf(octal_num, "%o", &decimal_num);
    return decimal_num;
}

int binary_to_decimal(char * binary_num) {
    int decimal_num = 0;
    int len = strlen(binary_num);
    for (int i = 0; i < len; i++) {
        if (binary_num[i] == '1') {
            decimal_num += 1 << (len - 1 - i);
        }
    }
    return decimal_num;
}