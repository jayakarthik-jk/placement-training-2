#include <stdio.h>

int main() {
    int a, b;
    printf("Enter the number a: ");
    scanf("%d", &a);
    printf("Enter the number b: ");
    scanf("%d", &b);
    int temp = a;
    a = b;
    b = temp;
    printf("number a: %d\n", a);
    printf("number b: %d\n", b);
}