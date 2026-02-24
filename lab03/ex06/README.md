## Exercício 06

(Divisível) Escreva um programa que leia um número inteiro positivo a partir do input (como uma sequência de caráteres até 100 chars) e que decide se o número lido é divisível por 9.

Se o número for divisível por 9, o programa deverá imprimir a mensagem `yes`, e deverá imprimir `no` no caso contrário.

*Atenção:* Os valores dos números podem ser superiores ao valor máximo do tipo `int` ou de qualquer tipo primitivo em C.

*Dica:* Um número é divisível por 9 se e só se a soma dos seus algarismos for divisível por 9. Por exemplo, a soma dos algarismos do número 729 é 18, pelo que é divisível por 9. O facto pode ser observado pela equação seguinte: 7 x 100 + 2 x 10 + 9 = (7 x 99 + __7__) + (2 x 9 + __2__) + 9.

**Input**
```
16
```

**Output**
```
no
```

**Input**
```
729
```

**Output**
```
yes
```
The results for the evaluation of this exercise can be found [here](https://gitlab.rnl.tecnico.ulisboa.pt/iaed/iaed26/feedback/labs/ist1117618/-/tree/master/lab03/ex06/README.md), in the feedback repository.
