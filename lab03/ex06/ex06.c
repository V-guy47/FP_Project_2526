/* iaed26 - ist1117618 - lab03/ex06 */
#include <stdio.h>

int main(){
    int soma = 0, valor;
    int car;
    while((car = getchar()) != EOF && car != '\n'){
        if(car >= '0' && car <= '9') {
            valor = car - '0';
            soma = soma + valor;
        }
        
    }
    if(soma % 9 == 0) {
        printf("yes\n");
    }
    else {
        printf("no\n");
    }
    return 0;
}