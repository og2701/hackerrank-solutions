using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        int n;
        string s;
        n = Convert.ToInt32(Console.ReadLine());
        for(int i=0; i<n; i++){
            s = Console.ReadLine();
            for(int j=0; j<s.Length; j+=2){
                Console.Write(s[j]);
            }
            Console.Write(' ');
            for(int j=1; j<s.Length; j+=2){
                Console.Write(s[j]);
            }
            Console.WriteLine();
        }
    }
}
