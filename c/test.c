#include <stdio.h>

int main() {
    char name[25] = "jk";
    char department[25];
    int total_subjects = 3;
    char subjects[3][25] = {
        "Java",
        "Android",
        "web development"
    };
    int questions_per_subject = 5;
    char questions[3][5][100] = {
        {
            "Number of primitive data types in Java are?",
            "What is the size of float and double in java?",
            "Automatic type conversion is possible in which of the possible cases?",
            "When an array is passed to a method, what does the method receive?",
            "When is the object created with new keyword?",
        },
        {
            "Android is",
            "For which of the following Android is mainly developed?",
            "Which of the following virtual machine is used by the Android operating system?",
            "Android is based on which of the following language?",
            " APK stands for ?",
        },
        {
            "What is HTML?",
            "Who is the father of HTML?",
            "HTML stands for __________",
            "What is the correct syntax of doctype in HTML5?",
            "Which of the following is used to read an HTML page and render it?",
        },
    };
    int options_per_question = 4;
    char options[3][5][4][100] = {
        {
            {
                "8",
                "6",
                "7",
                "4",
            },
            {
                "32 and 64",
                "32 and 32",
                "64 and 64",
                "64 and 32",
            },
            {
                "byte to int",
                "int to long",
                "long to byte",
                "short to byte",
            },
            {
                "array",
                "values of array",
                "copy of array",
                "referrence of array",
            },
            {
                "runtime",
                "compile time",
                "depends on code",
                "none",
            },
        },
        {
            {
                "operating system",
                "browser",
                "app",
                "website",
            },
            {
                "Servers",
                "Desktop",
                "laptop",
                "mobile",
            },
            {
                "JVM",
                "Dalvik virtual machine",
                "Simple virtual machine",
                "None",
            },
            {
                "Java",
                "C",
                "C++",
                "Python",
            },
            {
                "Android Phone Kit",
                "Android Page Kit",
                "Android Package Kit",
                "None",
            }
        },
        {
            {
                "HTML describes the structure of a webpage",
                "HTML is the standard markup language mainly used to create web pages",
                "HTML consists of a set of elements that helps the browser how to view the content",
                "All of the mentioned",
            },
            {
                "Rasmus Lerdorf",
                "Tim Berners-Lee",
                "Brendan Eich",
                "Sergey Brin",
            },
            {
                "HyperText Markup Language",
                "HyperText Machine Language",
                "HyperText Marking Language",
                "HighText Marking Language",
            },
            {
                "</doctype html>",
                "<doctype html>",
                "<doctype html!>",
                "<!doctype html>",
            },
            {
                "server",
                "network",
                "browser",
                "matrix",
            },
        },
    };
    int answer[3][5] = {
        {
            1,
            1,
            2,
            4,
            1
        },
        {
            1,
            4,
            2,
            1,
            3
        },
        {
            4,
            2,
            1,
            4,
            3
        },
    };
    int course_choice;
    int answer_choice;
    int mark = 0;
    printf("-----Online Test-----\n");
    printf("Enter the name: ");
    scanf("%s", name);
    printf("Enter the dept: ");
    scanf("%s", department);
    printf("Subjects\n");
    for (int i = 0; i < total_subjects; i++) {
        printf("\t%d. %s\n", i + 1, subjects[i]);
    }
    do {
        printf("Enter your subject choice: ");
        scanf("%d", &course_choice);
    } while(course_choice < 0 || course_choice > total_subjects);
    printf("\nWelcome to online session\n");
    printf("\n-----%s-----\n\n", subjects[course_choice - 1]);

    for(int i = 0; i < questions_per_subject; i++) {
        printf("%d. %s\n", i + 1, questions[course_choice - 1][i]);
        for(int j = 0; j < options_per_question; j++) {
            printf("\t%d. %s\n", j + 1, options[course_choice - 1][i][j]);
        }
        do {
            printf("\n\nEnter the correct option: ");
            scanf("%d", &answer_choice);
        } while(answer_choice < 0 || answer_choice > 4);
        if (answer_choice == answer[course_choice - 1][i])
        {
            printf("\n\nCorrect answer\n");
            mark++;
        } else {
            printf("\n\nwrong answer\n");
        }
    }
    printf("\n\nTotal marks out %d / 5 \n", mark);
    printf("\n\nthank you");
}