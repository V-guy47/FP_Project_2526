/* iaed26 - ist1117618 - lab02/ex08 */
#include <stdio.h>

int main() {
    int Num_var, cont = 0;
    float media, temp = 0, soma = 0;
    scanf("%d", &Num_var);
    while(cont < Num_var) {
        scanf("%f", &temp);
        soma = soma + temp;
        cont++;
    }
    media = soma / cont;
    printf("%.2f\n", media);
    return 0;
}