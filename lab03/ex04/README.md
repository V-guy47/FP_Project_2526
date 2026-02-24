## Exercício 04

(Números) Escreva um programa que leia uma sequência de números separados por espaços e novas linhas,
e imprima a mesma sequência, mas os números no output não deverão conter 0 no início, por exemplo, `007` deverá imprimir `7`.

A excepção é o número 0, que se deverá imprimir como 0.
A sequência no input termina com `EOF`.

*Atenção:* Os valores dos números poderão ser superiores ao valor máximo do tipo `int` ou qualquer tipo primitivo em C.

*Dica:* a função `int getchar()` pode ser usada para ler um carácter.

**Input**
```
01 3 02 000 027770
```

**Output**
```
1 3 2 0 27770
```
The results for the evaluation of this exercise can be found [here](https://gitlab.rnl.tecnico.ulisboa.pt/iaed/iaed26/feedback/labs/ist1117618/-/tree/master/lab03/ex04/README.md), in the feedback repository.
