#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARRAY_SIZE 160

char* readline();



int *factorial(int l, int *a, int n)
{
    int carry = 0;
    for (int i = 0; i < l; i++)
    {
        const int product = a[i] * n + carry; //product of the digit and carry

        a[i] = product % 10; //digit to 1s (units)
        carry = product / 10; //carry to the remainder of the product

        int j = i - 1; //previous of digit i

        while (carry != 0)
        {

            carry = a[j] + carry;//add carry to LHS
            a[j] = carry % 10;//LHS to 1s (units)
            carry = carry / 10;//update carry
            j--;
        }
    }


    return a;//returns factorial of i
}

void extraLongFactorials(int n)
{
    int r_len = ARRAY_SIZE, result[ARRAY_SIZE] = {0};//array of length 160 because length of 100! is 159
    result[ARRAY_SIZE - 1] = 1;//value of 1! in last index

    for (int i = 2; i <= n; i++)
    {
        memcpy(result, factorial(r_len, result, i), r_len);//copies factorial answer to result
    }



    int num_idx = 0;
    while (result[num_idx] == 0)//skips leading 0s
        num_idx++;


    for (; num_idx < r_len; num_idx++)//printing the answer digit by digit
    {
        printf("%d", result[num_idx]);
    }
}

int main()
{
    char* n_endptr;
    char* n_str = readline();
    int n = strtol(n_str, &n_endptr, 10);

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

    extraLongFactorials(n);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}
