/* iaed26 - ist1117618 - lab02/ex07 */
#include <stdio.h>

int main() {
    int num1, cont = 0, div = 1;
    scanf("%d", &num1);
    if (num1 < 0) {
        return 0;
    }
    else {
        for (div = 1; div <= num1; div++) {
            if (num1 % div == 0) {
                cont++;
            }
        }
        printf("%d\n", cont);
        return 0;
    }
}