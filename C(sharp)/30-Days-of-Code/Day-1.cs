using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        int i = 4;
        double d = 4.0;
        string s = "HackerRank ";

        int i2;
        double d2;
        string s2;
        // Declare second integer, double, and String variables.
        
        i2 = Convert.ToInt32(Console.ReadLine());
        d2 = Convert.ToDouble(Console.ReadLine());
        s2 = Console.ReadLine();
        // Read and save an integer, double, and String to your variables.
        
        Console.WriteLine(i+i2);
        // Print the sum of both integer variables on a new line.
        
        Console.WriteLine((d+d2).ToString("F1"));
        // Print the sum of the double variables on a new line.
        
        Console.WriteLine(s+s2);
        // Concatenate and print the String variables on a new line
        // The 's' variable above should be printed first.

    }
}
