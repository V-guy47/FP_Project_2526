/* iaed26 - ist1117618 - lab04/ex05 */
#include <stdio.h>
#include <string.h>

int leLinha(char s[]) {
    int i, c;
    c = getchar();
    for(i = 0; (c != '\n' && c != EOF); i++) {
        s[i] = c;
        c = getchar();
    }   
    s[i] = '\0';
    return i;
}

int main() {
    char s[80];

    leLinha(s);
    printf("%s", s);
    return 0;
    
} 