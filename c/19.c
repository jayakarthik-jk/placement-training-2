#include <stdio.h>

int main() {
    int length;
    printf("Enter the length: ");
    scanf("%d", &length);
    char number[length];
    printf("Enter the input: ");
    scanf("%s", number);
    if (number[length - 1] == '1') {
        printf("Odd");
    } else {
        printf("Even");
    }
    printf("\n");
}