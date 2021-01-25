import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        scanner.close();
        
        int[] reversedArray = reverseArr(n, arr);
        for(int i=0; i<n; i++){
            System.out.print(reversedArray[i]);
            System.out.print(' ');
        }
    }
    
    public static int[] reverseArr(int n, int[] arr)
    {
        int[] reversed = new int[n];
        for(int i=0; i<n; i++){
            reversed[i] = arr[n-1-i];
        }
        return reversed;
    }
}
