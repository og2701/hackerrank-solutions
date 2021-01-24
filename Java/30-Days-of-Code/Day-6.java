import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner inputs = new Scanner(System.in);
        Integer n = Integer.parseInt(inputs.nextLine());
        for(int i=0; i<n; i++){
            String s = inputs.nextLine();
            for(int j=0; j<s.length() ; j+=2){
                System.out.print(s.charAt(j));
            }
            System.out.print(" ");
            for(int j=1; j<s.length() ; j+=2){
                System.out.print(s.charAt(j));
            }
            System.out.print("\n");
        }
    }
}
