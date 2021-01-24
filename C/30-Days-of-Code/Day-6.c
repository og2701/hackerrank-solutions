#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    char s[65536];
    scanf("%d",&n);
    for(int i=0; i<n; i++){
        scanf("%s",s);
        for(int j=0; j<strlen(s); j+=2){
            printf("%c",s[j]);
        }
        printf(" ");
        for(int j=1; j<strlen(s); j+=2){
            printf("%c",s[j]);
        }
        printf("\n");
    }   
    return 0;
}
