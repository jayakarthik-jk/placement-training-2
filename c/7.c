#include <stdio.h>
int main() {
    char n;
    printf("Enter the character: ");
    scanf("%c", &n);
    if (n >= 65 && n <= 90)
        printf("Uppercase\n");
    else if (n >= 97 && n <= 122)
        printf("Lowercase\n");
    else
        printf("Not a character\n");
}