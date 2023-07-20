#include <stdio.h>

int main() {
    int n, first, last;
    printf("Enter the number: ");
    scanf("%d", &n);
    first = last =  n % 10;
    while (n != 0) {
        first = n % 10;
        n /= 10;

    }
    printf("first: %d\n", first);
    printf("last: %d\n", last);
}