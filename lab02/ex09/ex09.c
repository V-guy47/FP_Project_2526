/* iaed26 - ist1117618 - lab02/ex09 */
#include <stdio.h>

int main() {
    int seg, min, hor;
    scanf("%d", &seg);
    hor = seg / 3600;
    seg = seg % 3600;
    min = seg / 60;
    seg = seg % 60;
    printf("%02d:%02d:%02d", hor, min, seg); // FALTA O FORMATO HH:MM:SS
    return 0;
}