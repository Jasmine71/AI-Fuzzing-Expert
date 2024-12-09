#include <stdio.h>

void display_message() {
    printf("This is a message from b.c.\n");
}

int multiply(int x, int y) {
    return x * y;
}

int main() {
    display_message();
    int product = multiply(5, 6);
    printf("The result of multiplication is: %d\n", product);
    return 0;
}
