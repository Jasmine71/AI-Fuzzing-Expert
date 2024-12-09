#include <stdio.h>

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    printf("Calculating factorial in c.c.\n");
    int num = 5;
    printf("Factorial of %d is: %d\n", num, factorial(num));
    return 0;
}