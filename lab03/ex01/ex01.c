/* iaed26 - ist1117618 - lab03/ex01 */
#include <stdio.h>

void quadrado(int N) {
    int i, i2, cont = 0;
    for(i = 1; i <= N; i++) {
        for (i2 = 1 + cont; i2 <= N + cont; i2++) {
            printf("%d\t", i2);
        }
        printf("\n");
        cont++;
    }
}

int main() {
    int N = 0;
    while (N < 2) {
        scanf("%d", &N);
    }
    quadrado(N);
    return 0;
}