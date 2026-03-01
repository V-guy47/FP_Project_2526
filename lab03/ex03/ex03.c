/* iaed26 - ist1117618 - lab03/ex03 */
#include <stdio.h>

void cruz(int N) {
    int i,j;
    for(i = 0; i < N; i++) {
        for(j= 0; j < N; j++){
            if (i == j || i + j == N - 1) {
                printf("* ");
            }
            else {
                printf("- ");
            }
        }
        printf("\n");
    }
}
 
int main() {
    int Num;
    scanf("%d", &Num);
    cruz(Num);
}