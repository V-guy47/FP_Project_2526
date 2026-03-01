/* iaed26 - ist1117618 - lab03/ex04 */
#include <stdio.h>

int main() {
    int car, zeros = 0, numero1_9 = 0;
    while((car = getchar()) != EOF) {
        if(car == ' ' || car == '\n'){
            if(zeros != 0 && numero1_9 == 0){
                putchar('0');
            }
            putchar(car);
            zeros = 0; 
            numero1_9 = 0;
        }
        else if(car == '0'){
            if(numero1_9 == 0){
                zeros  = 1;
            }
            else {
                putchar(car);
            }
        }
        else if (car != '0') {
            numero1_9 = 1;
            putchar(car);
        }
        
    }
    return 0;
}