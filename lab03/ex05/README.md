## Exercício 05

(Mensagens) Escreva um programa que leia uma sequência de mensagens e imprima-as, uma por linha.
Cada mensagem é delimitada pelas aspas (carácter `"`). A mensagem pode conter uma "escape sequence" - o carácter perde significado especial se for precedido pelo caracter `\` (backslash). Por exemplo, o input `"a\"foo\\bar\""` corresponde à mensagem `a"foo\bar"`. Assim o backslash permite incluir aspas na mensagem tal como a própria backslash.

*Dica:* utilize o conceito de estado como fizemos no contador de palavras na aula teórica.

**Input**
```
"foo" "bar" "baz zap"
```

**Output**
```
foo
bar
baz zap
```
The results for the evaluation of this exercise can be found [here](https://gitlab.rnl.tecnico.ulisboa.pt/iaed/iaed26/feedback/labs/ist1117618/-/tree/master/lab03/ex05/README.md), in the feedback repository.
