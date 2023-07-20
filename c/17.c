#include <math.h>
#include <stdio.h>
int find_count(int n) {
    int digit_count;
    while (n != 0) {
        n /= 10;
        digit_count++;
    }
    return digit_count;
}

int main() {
    int n;
    int rev = 0;
    printf("Enter the number: ");
    scanf("%d", &n);
    int len = find_count(n);
    for (int i = 0; i < len; i++) {
        int j = n % 10;
        rev += pow(10, len - i - 1) * j;
        n /= 10;
    }
    
    printf("reversed: %d\n", rev);
}
