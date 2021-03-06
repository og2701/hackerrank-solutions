import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;



public class Solution {
    private static int result;

    public static void multiples(int n)
    {
        for(int i=1; i<=10; i++)
        {
            result = i*n;
            System.out.printf("%d x %d = %d\n",new Object[] {n,i,result});
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();
        
        multiples(n);
    }
}
