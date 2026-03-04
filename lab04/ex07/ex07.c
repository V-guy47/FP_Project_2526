/* iaed26 - ist1117618 - lab04/ex07 */
#include <stdio.h>
#include <string.h>

void apagaCaracter(char s[], char c) {
    int len = strlen(s);
    for(int i = 0; i < len; i++) {
        if (s[i] == c) {
            for(int j = i; j < len; j++) {
                s[j] = s[j + 1];
            }
            len--;
            i--;
        }
    }
}

int leLinha(char s[]) {
    int i, c;
    c = getchar();
    for(i = 0; (c != '\n' && c != EOF); i++) {
        s[i] = c;
        c = getchar();
    }   
    s[i] = '\0';
    return s[80];
}

int main() {
    char s[80], c;
    leLinha(s);
    scanf("%c", &c);
    apagaCaracter(s, c);
    printf("%s\n", s);
    return 0;
}