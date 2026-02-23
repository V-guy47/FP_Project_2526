/* iaed26 - ist1117618 - lab02/ex03 */
#include <stdio.h>

int main() {
    int num1, num2, num3;
    scanf("%d%d", &num1, &num2);
    num3 = num1 % num2;
    if (num3 == 0) {
        printf("yes\n");}
    else {
        printf("no\n");}
    return 0;
}