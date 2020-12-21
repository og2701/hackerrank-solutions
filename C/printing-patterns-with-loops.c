#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

int main() 
{

    int n;
    scanf("%d", &n);
  	
    for(int i=1-n; i<n; i++){
        for(int j=1-n; j<n; j++){
            printf("%d ",MAX(abs(i),abs(j))+1);
        }
        printf("\n");
    }  
      
    return 0;
}
