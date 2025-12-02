#include <stdio.h>

int main() {

    float a, b, media;

    printf("Inserisci il primo numero: ");
    scanf("%f", &a);

    printf("Inserisci il secondo numero: ");
    scanf("%f", &b);

    media = (a + b) / 2;

    if (media == (int)media) {
        printf("La media e': %d\n", (int)media);

    } else {
        printf("La media e': %.2f\n", media);
        
    }

    return 0;
}