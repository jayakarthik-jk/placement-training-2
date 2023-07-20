#include <stdio.h>
int range_sum(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += i;
    }
    return sum;
}
int main() {
    int n;
    printf("enter the number: ");
    scanf("%d", &n);
    printf("%d\n",  range_sum(n));
}
