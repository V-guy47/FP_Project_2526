/* iaed26 - ist1117618 - lab04/ex04 */
#include <stdio.h>
#include <string.h>
#define MAX 80

int main () {
    char s[MAX], b = 1;
    int i;
    scanf("%s", s);
    for(i = 0; b && i < (int)strlen(s)/2; i++) {
        b = (s[i] == s[strlen(s) - i - 1]);
    }
    printf("%s", b ? "yes\n" : "no\n");
    return 0;
}