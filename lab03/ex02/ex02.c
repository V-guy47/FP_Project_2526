/* iaed26 - ist1117618 - lab03/ex02 */
#include <stdio.h>

void piramide(int N) {
    int i, cont_esp = 0, j;
    for(i = 1; i <= N; i++) {
        cont_esp = 2*(N - i);
        printf("%*s", cont_esp, "");
        for (j = 1; j < i; j++) {
            printf("%d ", j);
        }
        for (j = i; j > 1; j--) {
            printf("%d ", j);
        }
        printf("1\n");
    }
}

int main() {
    int N = 0;
    while (N < 2) {
        scanf("%d", &N);
    }
    piramide(N);
    return 0;
}