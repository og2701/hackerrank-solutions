#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";

    int i2;
    double d2;
    char s2[100];
    // Declare second integer, double, and String variables.
    
    scanf("%d%lf\n",&i2,&d2);
    scanf ("%[^\n]s", &s2);
    // Read and save an integer, double, and String to your variables.
    
    printf("%d\n",i+i2);
    // Print the sum of both integer variables on a new line.
    
    printf("%.1f\n",d+d2);
    // Print the sum of the double variables on a new line.
    
    printf("%s%s\n",s,s2);
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.

    return 0;
}
