// complex_example.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Global variables
int global_var1;
char global_var2[50];

// Function declarations
void func1();
int func2(int a, int b);

int main() {
    // Local variables
    int local_var1 = 10;
    char local_var2[20];

    // Function calls
    func1();
    int result = func2(local_var1, 20);

    // libc calls
    printf("Result: %d\n", result);
    strcpy(local_var2, "Hello, World!");

    // If conditions
    if (result > 0) {
        printf("Positive result\n");
    } else {
        printf("Non-positive result\n");
    }

    // Loops
    for (int i = 0; i < 10; i++) {
        printf("Loop iteration: %d\n", i);
    }

    return 0;
}

void func1() {
    // Local variable
    int local_var3 = 5;
    printf("In func1, local_var3: %d\n", local_var3);
}

int func2(int a, int b) {
    // Local variable
    int local_var4 = a + b;
    return local_var4;
}