#include <stdio.h>

int main() {
    int numero;
    int numero2;
    int moltiplicazione;

    printf("Inserisci un numero intero:\n");
    scanf("%d", &numero);

    printf("Inserisci un altro numero intero:\n");
    scanf("%d", &numero2);

    moltiplicazione = numero * numero2; 

    printf("La moltiplicazione di %d e %d e': %d\n", numero, numero2, moltiplicazione);
    
    return 0;
}