#include <stdio.h>
#include <stdlib.h>
#include <windows.h>   // for Sleep() function

void TOP();
void Right();
void BOTTOM();
void Left();

int main() {
    while (1) {
        TOP();
        Sleep(400);
        system("cls");
        Right();
        Sleep(400);
        system("cls");
        BOTTOM();
        Sleep(400);
        system("cls");
        Left();
        Sleep(400);
        system("cls");
    }
    return 0;
}

void TOP() {
    int n, Row, x, y;
    for (n = 0; n < 3; n++) {
        printf("\t\t\t\t\n");
    }
    for (Row = 0; Row < 7; Row++) {
        printf("\t\t\t\t");
        for (x = Row; x < 7; x++) {
            printf(" ");
        }
        for (y = 0; y < (2 * Row) - 1; y++) {
            printf("*");
        }
        printf("\n");
    }
    for (int i = 0; i < 7; i++) {
        printf("\t\t\t\t      *\n");
    }
}

void Right() {
    int n, Row, x;
    for (n = 0; n < 10; n++) {
        printf("\t\t\t\t\n");
    }
    for (Row = 0; Row < 6; Row++) {
        printf("\t\t\t\t\t\t        ");
        for (x = 0; x < Row; x++) {
            printf("*");
        }
        printf("\n");
    }
    printf("\t\t\t\t      * * * * * * * * * * * *\n");
    for (Row = 0; Row < 6; Row++) {
        printf("\t\t\t\t\t\t        ");
        for (x = Row; x < 5; x++) {
            printf("*");
        }
        printf("\n");
    }
}

void BOTTOM() {
    int n, Row, x, y;
    for (n = 0; n < 16; n++) {
        printf("\t\t\t\t\n");
    }
    for (int i = 0; i < 7; i++) {
        printf("\t\t\t\t      *\n");
    }
    for (Row = 1; Row < 7; Row++) {
        printf("\t\t\t\t ");
        for (x = 1; x < Row; x++) {
            printf(" ");
        }
        for (y = 0; y < (14 - (2 * Row) - 1); y++) {
            printf("*");
        }
        printf("\n");
    }
}

void Left() {
    int n, Row, x, y;
    for (n = 0; n < 11; n++) {
        printf("\t\n");
    }
    for (Row = 1; Row < 6; Row++) {
        printf("\t       ");
        for (y = Row; y < 6; y++) {
            printf(" ");
        }
        for (x = 0; x < Row; x++) {
            printf("*");
        }
        printf("\n");
    }
    printf("\t        * * * * * * * * * * * *\n");
    for (Row = 1; Row < 6; Row++) {
        printf("\t        ");
        for (y = 1; y < Row; y++) {
            printf(" ");
        }
        for (x = Row; x < 6; x++) {
            printf("*");
        }
        printf("\n");
    }
}