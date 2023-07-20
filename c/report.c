#include <stdio.h>

int SIZE = 5;
int main() {
    char name[25];
    int marks[SIZE];
    int total = 0;
    printf("Enter the name: ");
    scanf("%s", name);
    printf("Enter the marks\n");
    for (int i = 0; i < SIZE; i++) {
        do {
            printf("Enter the mark for Subject %d: ", i + 1);
            scanf("%d", &marks[i]);
        } while(marks[i] < 0 && marks[i] > 100);
        total += marks[i];
    }
    
    printf("<-----Report Card----->\n");
    printf("Name: %s\n", name);
    printf("-----Grades-----\n");
    for (int i = 0; i < SIZE; i++) {
        switch (marks[i] / 10)
        {
        case 10:
        case 9:
            printf("Subject %d: Grade O", i + 1);
            break;
        case 8:
            printf("Subject %d: Grade A+", i + 1);
            break;
        case 7:
            printf("Subject %d: Grade A", i + 1);
            break;
        case 6:
            printf("Subject %d: Grade B+", i + 1);
            break;
        case 5:
            printf("Subject %d: Grade B", i + 1);
            break;
        default:
            printf("Subject %d: Failed", i + 1);
            break;
        }
        printf("\n");
    }
    printf("Total: %d\n", total);
    printf("Average: %d\n", total / SIZE);
    
}
