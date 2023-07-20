#include <stdio.h>

int main() {
    int trainee_oxygen_levels[3][3];
    printf("Enter the inputs: \n");
    int averages[3] = { 0, 0, 0 };
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            scanf("%d", &trainee_oxygen_levels[i][j]);
            if(trainee_oxygen_levels[i][j] > 100 || trainee_oxygen_levels[i][j] < 0) {
                printf("Invalid Oxygen level\n");
                return 0;
            }
            averages[j] += trainee_oxygen_levels[i][j];
        }
    }
    int max = 0;
    for (int i = 0; i < 3; i++) {
        averages[i] = averages[i] / 3;
        if(averages[i] > max) {
            max = averages[i];            
        }
    }

    if(max < 70) {
        printf("all players are unfit\n");
        return 0;
    }
    for (int i = 0; i < 3; i++) {
        if (max == averages[i]) {
            printf("Player %d is fit\n", i + 1);   
        }
    }
    

    return 0;
}