#include <stdio.h>
int main() {
    char n;
    printf("Enter the character: ");
    scanf("%c", &n);
    if (n == 'a' || n == 'e' || n == 'i' || n == 'o' || n == 'u')
        printf("Vowels\n");
    else
        printf("Consonents\n");
}