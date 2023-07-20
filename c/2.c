#include <stdio.h>
int main() {
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    if (n < 0)
        printf("Negative\n");
    else if (n > 0)
        printf("Positive\n");
    else
        printf("Zero\n");
}