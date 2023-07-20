
#include <stdio.h>

int main() {
    int baloons_colors[] = { 0, 0, 0, 0 };
    int total_baloons;
    printf("Enter the number of baloons: ");
    scanf("%d", &total_baloons);
    char ballons[total_baloons];
    char latest_odd_baloon = '\0';
    for (int i = 0; i < total_baloons; i++) {
        printf("Enter baloon %d color: ", i + 1);
        scanf("\n%c", &ballons[i]);
        switch(ballons[i]) {
            case 'r':
            if (baloons_colors[0] == 0) {
                baloons_colors[0] = 1;
            } else {
                baloons_colors[0] = 0;
            }
            break;
            case 'g':
            if (baloons_colors[1] == 0) {
                baloons_colors[1] = 1;
            } else {
                baloons_colors[1] = 0;
            }
            break;
            case 'b':
            if (baloons_colors[2] == 0) {
                baloons_colors[2] = 1;
            } else {
                baloons_colors[2] = 0;
            }
            break;
            case 'y':
            if (baloons_colors[3] == 0) {
                baloons_colors[3] = 1;
            } else {
                baloons_colors[3] = 0;
            }
            break;
            default:
            printf("Invalid Input\n");
            return 0;
        }
    }

    for (int i = 0; i < total_baloons; i++) {
        if (ballons[i] == 'r' && baloons_colors[0] == 1) {
            printf("Red is odd\n");
            return 0;
        }
        if (ballons[i] == 'g' && baloons_colors[1] == 1) {
            printf("green is odd\n");
            return 0;
        }
        if (ballons[i] == 'b' && baloons_colors[2] == 1) {
            printf("blue is odd\n");
            return 0;
        }
        if (ballons[i] == 'y' && baloons_colors[3] == 1) {
            printf("yellow is odd\n");
            return 0;
        }
    }
    printf("Every thing is even\n");    
    return 0;
}