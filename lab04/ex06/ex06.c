/* iaed26 - ist1117618 - lab04/ex06 */
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
    return s[1000];
}

void maiusculas(char s[]) {
    int c, len = strlen(s);
    for(int i = 0; i < len; i++) {
        if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] += ('A' - 'a');
        }
    }
}

int main() {
    char s[1000];

    leLinha(s);
    maiusculas(s);
    printf("%s", s);
    return 0;
    
} 