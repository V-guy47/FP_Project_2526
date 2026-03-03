/* iaed26 - ist1117618 - lab04/ex02 */
#include <stdio.h>
#define VECMAX 100

int main() {
    int n = -1, v[VECMAX], i, j, max = -1;
    while(n > VECMAX || n < 0) {
        scanf("%d", &n);
    }
    for(i = 0; i < n; i++) {
        scanf("%d", &v[i]);
        if(v[i] > max) {
            max = v[i];
        }
    }
    for(i = 0; i < max; i++) {
        for(j = 0; j < n; j++) {
            if (v[j] > 0) {
                putchar('*');
                v[j]--;
            }
            else{
                putchar(' ');
            }
        }
        putchar('\n');
    }
    return 0;
}