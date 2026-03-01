/* iaed26 - ist1117618 - lab03/ex07 */
#include <stdio.h>
int main() {
    int first, acc;
    char car;
    scanf("%d %c %d", &first, &car, &acc);
    first = (car == '+' ? first + acc : first - acc);
    while(scanf(" %c %d", &car, &acc) == 2) {
        first = (car == '+' ? first + acc : first - acc);
    }
    printf("%d\n", first);
    return 0;
}