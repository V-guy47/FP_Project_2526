/* iaed26 - ist1117618 - lab02/ex10 */
#include <stdio.h>

int main() {
    int num, soma = 0, cont = 0, resto;
    scanf("%d", &num);
    while (num > 0) {
        resto = num % 10;
        cont++;
        soma = soma + resto;
        num = num / 10;

    }
    printf("%d\n%d", cont, soma);
    return 0;
}