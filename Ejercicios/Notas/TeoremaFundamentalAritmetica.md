<img width="890" height="594" alt="image" src="https://github.com/user-attachments/assets/9d077add-571f-41be-8c03-de5288aa1b35" />

<img width="954" height="244" alt="image" src="https://github.com/user-attachments/assets/19ca43c4-e4a7-4659-b32f-83bc683f537b" />

## Por ejemplo:
198 = 3^2 * 2^1 * 11^1

## Patrón:
### Para exponentes 1
Dado un número n y su configuración prima, para sacar el número de divisores de n:

Los números en corchetes son los exponentes de cada número primo...

- e = [1] -> 2 divisores
- e = [1, 1] -> 4 divisores
- e = [1, 1, 1] -> 8 divisores
- e = [1, 1, 1, 1] -> 16 divisores
- e = [1, 1, 1, 1, 1] -> 32 divisores

Osea, dado n = p1^1 * p2^1 * pk^1

El número de divisores es: 2^k

### Para exponentes k y 1
- e = [2, 1, 1]

  **exp_1 = [1, 1]  ->  2^2 = 4 divisores**

  Pero para el exponente k:

  **p^2 -> 3 divisores**

  p^4 -> 5 divisores

  p^5 -> 6 divisores

  p^17 -> 18 divisores

  p^k -> k + 1 divisores

Entonces:

Para e = [2, 1, 1] -> 4 * 3 = 12 divisores

## En general:
<img width="596" height="262" alt="image" src="https://github.com/user-attachments/assets/314e1ed6-0680-4e9d-8f74-729ac51f99ac" />
