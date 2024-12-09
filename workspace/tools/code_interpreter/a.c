#include <stdio.h>

void greet() {
    printf("Hello from a.c!\n");
}

int add(int x, int y) {
    return x + y;
}

int main() {
    greet();
    int result = add(3, 4);
    printf("The result of addition is: %d\n", result);
    return 0;
}
