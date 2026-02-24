/* iaed26 - ist1117618 - lab02/ex06 */
#include <stdio.h>

int main() {
    int n, i = 1;
    float min, max, temp;
    scanf("%d", &n);
    scanf("%f", &max);
    min = max;
    while(i < n) {
        scanf("%f", &temp);
        if (temp < min) {
            min = temp;}
        if (temp > max) {
            max = temp;}
        i++;
    }
    printf("min: %f, max: %f\n", min, max);
    return 0;
}