#include <stdio.h>

int main() {
    int n;
    int p;
    int r = 1;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("Enter the power: ");
    scanf("%d", &p);
    for (int i = 0; i < p; i++) {
        r *= n; 
    }
    printf("Result: %d\n", r);
}
