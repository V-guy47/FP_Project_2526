/* iaed26 - ist1117618 - lab02/ex04 */
#include <stdio.h>

int main() {
    int a, b, c, aux;
    scanf("%d%d%d", &a, &b, &c);
    if (a > b) {
        aux = a;
        a = b;
        b = aux;
    }
    if (c < b) {
        aux = c;
        c = b;
        b = aux;
        if (b < a) {
            aux = a;
            a = b;
            b = aux;
        }
    }
    printf("%d %d %d", a, b, c);
    return 0;
}