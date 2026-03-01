/* iaed26 - ist1117618 - lab03/ex05 */
#include <stdio.h>
#include <stdbool.h>

int main() {
    int car;
    bool entre_aspas = false, depois_da_barra = false;
    int cont = 0;
    while((car = getchar()) != EOF){
        if(depois_da_barra) {
            putchar(car);
            depois_da_barra = false;
            continue;
        }
        else if (car == '"' && !entre_aspas){
            entre_aspas = true;
            continue;
        }
        else if (entre_aspas){
            if (car == '"') {
                entre_aspas = false;
                putchar('\n');
            }
            else if(car == '\\'){
                depois_da_barra = true;
                continue;
            }
            else {
                putchar(car);
            }
        }
    }
    return 0;
}