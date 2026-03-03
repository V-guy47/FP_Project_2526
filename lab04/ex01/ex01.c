/* iaed26 - ist1117618 - lab04/ex01 */
#include <stdio.h>
#define VECMAX 100

int main() {
    int num = 1000, num_ast, i, j;
    while(num > VECMAX || num < 0) {
        scanf("%d", &num);
    }
    for(i = 0;  i < num; i++) {
        scanf("%d", &num_ast);
        for(j = 0; j < num_ast; j++) {
        printf("*");
        }
        printf("\n");
    }
    
}