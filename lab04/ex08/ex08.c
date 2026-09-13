/* iaed26 - ist1117618 - lab04/ex08 */
#include <stdio.h>
#include <string.h>

int main() {
    char num1[80], num2[80], estado = 0;
    int len;
    scanf("%80s", num1);
    scanf("%80s", num2);
    len = strlen(num1); // os dois tem o mesmo comprimento

    for(int i = 0; i < len; i++) {
        if(num1[i] > num2[i]) {
            estado = 0;
            break;
        }
        else if (num1[i] < num2[i]) {
            estado = 1;
            break;
        }
    }
    if (estado) {
        printf("%s\n", num2);
    }
    else {
        printf("%s\n", num1);
    }

}