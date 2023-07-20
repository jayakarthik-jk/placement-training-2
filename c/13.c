#include <stdio.h>

int main() {
    int digit_count = 0;
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    while (n != 0) {
        n /= 10;
        digit_count++;
    }
    printf("total digits: %d\n", digit_count);
}