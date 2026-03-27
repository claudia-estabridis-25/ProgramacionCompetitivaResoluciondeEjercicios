## Función generadora

El día de hoy Wayki encontró la siguiente serie aritmética: 5, 8, 11, 14, .... Pero lo más importante que notó es que estos números pudieron generarse con
la función f(n) = 2 + 3*n, donde n (n>=1) representa el número de término en la serie (el término 1 es el 5, el término 2 es el 8 y así sucesivamente).

Ahora dada la función f(n) = a + b*n, que genera una serie aritmética, Wayki le pide ayuda para saber si el número x es parte de dicha serie.

### Input Format
La entrada consiste de 3 enteros a, b y x, descritos anteriormente.

### Constraints
1 <= a,b <= 1000
1 <= x <= &10^7&

#### Output Format
Imprimir "SI" si  es parte de la serie aritmética, en caso contrario imprimir "NO".

### Sample Input 0
1 5 11

### Sample Output 0
SI

### Explanation 0
Para a = 1 y b = 5 la serie que se forma es: 6, 11, 16, 21,... Por lo tanto, 11 sería el 2do término de la serie.

### Sample Input 1
3 2 1

### Sample Output 1
NO
