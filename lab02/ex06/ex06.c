/* iaed26 - ist1117618 - lab02/ex06 */
#include <stdio.h>

int main() {
    int n, i = 0;
    float min, max, temp;
    scanf("%d %f", &n, &max);
    min = max;
    while(n <= i) {
        scanf("%f", &temp);
        if (temp < min) min = temp;
        if (temp > max) max = temp;
        i++;
    }
    printf("min: %f, max: %f\n", min, max);
    return 0;
}